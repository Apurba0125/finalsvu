"""Every page of the site is built here.

There is no database in this build.  Each view takes what it needs from
``website/data.py``, decorates it (URLs, real ``date`` objects, pagination) and
renders a template.  When the content later moves into models, the templates
stay exactly as they are and only the lookups in this file change.
"""
import datetime
import logging
import os
import re

from django.conf import settings
from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.template import TemplateDoesNotExist
from django.templatetags.static import static as static_url
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.text import slugify
from django.views.decorators.http import require_GET, require_POST

from . import captcha, data
from .templatetags.svu_extras import doc_url
from .forms import ContactForm, EnquiryForm

logger = logging.getLogger(__name__)

PAGE_SIZE = 9


# ---------------------------------------------------------------- helpers
def _as_date(value):
    """'2026-05-23' -> ``datetime.date(2026, 5, 23)``; pass anything else through."""
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value
    try:
        return datetime.datetime.strptime(str(value)[:10], "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def _events():
    """Events, newest first, with a resolved URL and a real date."""
    items = []
    for row in data.EVENTS:
        item = dict(row)
        item["event_date"] = _as_date(row.get("event_date"))
        item["url"] = reverse("website:event_detail", args=[row["slug"]])
        items.append(item)
    items.sort(key=lambda e: e["event_date"] or datetime.date.min, reverse=True)
    return items


def _notices():
    items = []
    for row in data.NOTICES:
        item = dict(row)
        item["date"] = _as_date(row.get("date"))
        # No page per notice: the board is where they all live.
        item["url"] = reverse("website:notice_list")
        # Optional PDF. _asset resolves it through the static manifest and
        # returns "" when the file was never collected, so a mistyped path
        # costs the attachment rather than the whole notice.
        item["document"] = _asset(row.get("document"))
        item["document_label"] = (row.get("document_label")
                                  or "Download the notice (PDF)")
        items.append(item)
    items.sort(key=lambda n: n["date"] or datetime.date.min, reverse=True)
    return items


def _schools():
    items = []
    for row in data.SCHOOLS:
        item = dict(row)
        item["url"] = reverse("website:school_detail", args=[row["slug"]])
        items.append(item)
    return items


def _departments(school=None):
    """Departments, each carrying the school it belongs to.

    ``school`` narrows the list to one school slug, which is what the school
    page needs when it lists its own departments.
    """
    school_names = {s["slug"]: s["name"] for s in data.SCHOOLS}
    school_images = {s["slug"]: s.get("card_image", "") for s in data.SCHOOLS}
    items = []
    for row in data.DEPARTMENTS:
        if school and row["school"] != school:
            continue
        item = dict(row)
        item["url"] = reverse("website:department_detail", args=[row["slug"]])
        item["school_name"] = school_names.get(row["school"], "")
        # The photograph beside the intro. A department that has not been given
        # one of its own borrows its school's card image, and the generic
        # placeholder only appears if that is missing too - so the layout never
        # collapses around a hole while the real photographs are collected.
        item["image"] = (_asset(row.get("image"))
                         or _asset(school_images.get(row["school"], ""))
                         or _asset("img/school-placeholder.svg"))
        item["school_url"] = (
            reverse("website:school_detail", args=[row["school"]])
            if row["school"] in school_names else ""
        )
        item["course_count"] = sum(1 for c in data.COURSES
                                   if c["department"] == row["slug"])
        items.append(item)
    return items


# --------------------------------------------------------------------------
# Files named after the course they belong to, so that dropping one in is the
# whole job and there is no line to edit in data.py:
#
#     static/img/courses/b-tech-in-civil-engineering.jpg        <- its picture
#     static/documents/syllabus/b-tech-in-civil-engineering.pdf <- its syllabus
#
# The name is the course's SLUG - the last part of its URL. Each folder has a
# README saying so, for whoever is adding the files.
#
# Neither is compulsory. A course with no picture falls back to its
# department's and then its school's; a course with no syllabus simply shows
# no Download Syllabus button, rather than one that leads to a 404. What is
# written on the course row in data.py beats a file found by name.
COURSE_IMAGE_DIR = "img/courses"
COURSE_IMAGE_TYPES = (".jpg", ".jpeg", ".png", ".webp")

COURSE_SYLLABUS_DIR = "documents/syllabus"
COURSE_SYLLABUS_TYPES = (".pdf",)

_slug_named_index = {}


def _slug_named_files(folder, extensions):
    """``{slug: '<folder>/<file>'}`` for what is sitting in a static folder.

    Read once per process and kept, except under DEBUG where it is read again
    every time: adding a picture or a PDF is not a code change, so the dev
    server does not restart for it, and a cached listing would leave whoever
    added the file staring at the old page wondering what went wrong.
    """
    if not settings.DEBUG and folder in _slug_named_index:
        return _slug_named_index[folder]

    index = {}
    for root in settings.STATICFILES_DIRS:
        path = os.path.join(str(root), *folder.split("/"))
        try:
            names = sorted(os.listdir(path))
        except OSError:
            # No such folder yet, which is the normal state until the first
            # file is dropped in.
            continue
        for name in names:
            stem, extension = os.path.splitext(name)
            if extension.lower() in extensions:
                # setdefault over a sorted listing, so with both a .jpg and a
                # .png of the same course the answer is the same every time
                # rather than following the order the filesystem hands them
                # back.
                index.setdefault(stem.lower(), "%s/%s" % (folder, name))

    _slug_named_index[folder] = index
    return index


def _courses():
    school_names = {s["slug"]: s["name"] for s in data.SCHOOLS}
    school_images = {s["slug"]: s.get("card_image", "") for s in data.SCHOOLS}
    department_names = {d["slug"]: d["name"] for d in data.DEPARTMENTS}
    department_images = {d["slug"]: d.get("image", "") for d in data.DEPARTMENTS}
    program_names = {p["slug"]: p["name"] for p in data.PROGRAMS}
    items = []
    for row in data.COURSES:
        item = dict(row)
        item["url"] = reverse("website:course_detail", args=[row["slug"]])
        item["school_name"] = school_names.get(row["school"], "")
        # Finest first: the picture named on the course row, then one named
        # after the course in static/img/courses/ (_slug_named_files above),
        # then its department's, then its school's, then the placeholder.
        #
        # Every listing on the site reads this one value - the course cards on
        # a department page as much as the course page itself - so a course
        # cannot show one picture in one place and another somewhere else.
        item["card_image"] = (_asset(row.get("card_image"))
                              or _asset(_slug_named_files(
                                  COURSE_IMAGE_DIR, COURSE_IMAGE_TYPES)
                                  .get(row["slug"], ""))
                              or _asset(department_images.get(row["department"], ""))
                              or _asset(school_images.get(row["school"], ""))
                              or _asset("img/school-placeholder.svg"))
        # The banner behind the course title. A ladder of its own, NOT
        # card_image's, because the two want different pictures:
        #
        #   this one   the course's own banner, then its school's, then the
        #              campus shot everything else falls back to
        #
        # Deliberately NOT the school card_image the intro band uses. Those
        # carry the school name and crest painted into the picture, and a
        # banner is so much wider than it is tall that cropping to it cuts
        # the wording in half behind the title — a Computer Science course
        # came out reading "School of Engineering" across its middle. A
        # banner wants a picture with nothing important in the centre.
        item["hero_image"] = (_asset(row.get("hero_image"))
                              or _asset(data.COURSE_BANNERS.get(row["school"], ""))
                              or _asset("img/about/team.png"))
        # The PDF behind the Download Syllabus button on the eligibility tab.
        # 'syllabus' on the course row first - through doc_url, so a path
        # typed before the file exists hides the button instead of taking the
        # page down - then a PDF named after the course.
        item["syllabus_url"] = (doc_url(row.get("syllabus", ""))
                                or _asset(_slug_named_files(
                                    COURSE_SYLLABUS_DIR, COURSE_SYLLABUS_TYPES)
                                    .get(row["slug"], "")))
        item["department_name"] = department_names.get(row["department"], "")
        item["program_name"] = program_names.get(row["program"], "")
        item["school_url"] = (
            reverse("website:school_detail", args=[row["school"]])
            if row["school"] in school_names else ""
        )
        item["department_url"] = (
            reverse("website:department_detail", args=[row["department"]])
            if row["department"] in department_names else ""
        )
        items.append(item)
    return items


def _find(items, slug, key="slug"):
    for item in items:
        if item.get(key) == slug:
            return item
    return None


def _paginate(request, items):
    paginator = Paginator(items, PAGE_SIZE)
    return paginator.get_page(request.GET.get("page"))


def _nav_title(path):
    """Look up a menu label for a URL, so placeholder pages get a real heading."""
    for entry in data.MAIN_NAV:
        if entry["href"] == path:
            return entry["title"]
        # A menu entry with no dropdown may simply omit 'children'; insisting
        # on the key here took every placeholder page down with a KeyError.
        for child in entry.get("children") or []:
            if child["href"] == path:
                return child["title"]
    # FOOTER_LINKS is a list of columns, each with its own 'links'.
    footer = [link for column in data.FOOTER_LINKS for link in column["links"]]
    for entry in data.TOP_NAV + footer:
        if entry.get("href") == path or entry.get("url") == path:
            return entry["title"]
    return ""


def _fresh_captcha(form=None):
    token, image = captcha.issue()
    if form is not None:
        form.fields["captcha_token"].initial = token
    return token, image


def _enquiry_context(form=None):
    """Bound-or-blank enquiry form plus a freshly issued CAPTCHA."""
    form = form or EnquiryForm()
    token, image = _fresh_captcha(form)
    return {"enquiry_form": form, "captcha_token": token, "captcha_image": image}


# ---------------------------------------------------------------- homepage
HOME_EVENT_COUNT = 8


def _home_events(events):
    """Featured events first, then the newest of the rest.

    Taking *only* the featured ones left the slider with exactly as many
    cards as fit across the screen, so it had nothing to scroll and its
    arrows sat permanently disabled.  Topping the list up keeps it moving
    while the flagged events still lead.
    """
    featured = [e for e in events if e["is_featured"]]
    rest = [e for e in events if not e["is_featured"]]
    return (featured + rest)[:HOME_EVENT_COUNT]


def home(request):
    events = _events()
    context = {
        "hero_video": data.HERO_VIDEO,
        "notices": _notices()[:5],
        "quick_links": data.QUICK_LINKS,
        "enlistments": data.ENLISTMENTS,
        "affiliations": data.AFFILIATIONS,
        "recruiters": data.RECRUITERS,
        "life_at_svu": data.LIFE_AT_SVU,
        "offerings": data.OFFERINGS,
        "schools": _schools(),
        "videos": data.VIDEOS,
        "stats": data.STATS,
        "events": _home_events(events),
        # CHANCELLOR is commented out in data.py for now — the band hides
        # itself rather than taking the homepage down with it.
        "chancellor": getattr(data, "CHANCELLOR", None),
        # Six on the home slider; the rest live on the page behind View All,
        # which is written by hand.
        "appreciations": data.APPRECIATIONS[:6],
        "testimonials": data.TESTIMONIALS,
    }
    context.update(_enquiry_context())
    return render(request, "pages/home.html", context)


# ---------------------------------------------------------------- academics
NUMBER_WORDS = ["No", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                "Eight", "Nine", "Ten", "Eleven", "Twelve"]


def _count_word(number):
    """3 -> 'Three'.  Falls back to the digits once past the table."""
    return NUMBER_WORDS[number] if number < len(NUMBER_WORDS) else str(number)


def school_list(request):
    schools = _schools()
    return render(request, "pages/school_list.html", {
        "schools": schools,
        "hero_title": "Our Schools",
        # Counted from SCHOOLS rather than written out, so adding or removing a
        # school never leaves the wrong number on the page.
        "hero_subtitle": "%s schools covering engineering, management, sciences, agriculture, "
                         "computer science, health, humanities and law."
                         % _count_word(len(schools)),
        # The banner photograph. page_hero.html lays it over the dark ground at
        # low opacity, which is what keeps the white title readable — swap the
        # file name here and that is the whole edit.
        "hero_image": "img/about/team.png",
        "crumbs": [{"label": "Academics"}, {"label": "Our Schools"}],
    })


def school_detail(request, slug):
    school = _find(data.SCHOOLS, slug)
    if not school:
        return error_404(request, None)

    # A school lists its departments, and each department carries its own
    # courses — school -> department -> course, the way the academics tree runs.
    courses = [c for c in _courses() if c["school"] == slug]
    departments = _departments(school=slug)
    for department in departments:
        department["courses"] = [c for c in courses
                                 if c["department"] == department["slug"]]

    return render(request, "pages/school_detail.html", {
        "school": school,
        "departments": departments,
        "courses": courses,
        "programs": [p for p in data.PROGRAMS
                     if any(c["program"] == p["slug"] for c in courses)],
        "hero_title": school["name"],
        "hero_subtitle": school["short_description"],
        "hero_image": school["card_image"],
        "crumbs": [
            {"label": "Academics"},
            {"label": "Our Schools", "url": reverse("website:school_list")},
            {"label": school["name"]},
        ],
    })


def _asset(value):
    """Turn a data.py asset reference into something usable in ``href``/``src``.

    ``'img/faculty/cv.pdf'``      -> ``'/static/img/faculty/cv.pdf'``
    ``'https://example.com/cv'``  -> unchanged
    ``'/page/our-team/'``         -> unchanged

    Without this a bare static path would be read as a relative link and
    resolve against the current page, which 404s.
    """
    if not value:
        return ""
    if value.startswith(("http://", "https://", "//", "/", "mailto:", "tel:")):
        return value
    try:
        return static_url(value)
    except ValueError:
        # With DEBUG off the manifest storage raises rather than handing back a
        # URL for a file that was never collected. Treat that the same as no
        # value at all: the templates already hide an empty photo or profile
        # link, so a typo in data.py costs that one link instead of returning
        # 500 for the whole department. The warning is what makes it findable.
        logger.warning("data.py refers to a static file that does not exist: %r",
                       value)
        return ""


def _faculty(slug):
    """Faculty for a department, with photo and profile links resolved."""
    people = []
    for row in data.DEPARTMENT_FACULTY.get(slug, []):
        person = dict(row)
        person["photo"] = _asset(row.get("photo"))
        person["profile_url"] = _asset(row.get("profile_url"))
        # A PDF should open in its own tab; an internal page should not.
        person["is_file"] = person["profile_url"].lower().endswith(
            (".pdf", ".doc", ".docx"))
        people.append(person)
    return people


def _department_tabs(department):
    """Tab panels for a department, falling back to the generic set.

    The default copy carries a ``{department}`` placeholder so a department
    with no bespoke text still reads as its own page.
    """
    tabs = data.DEPARTMENT_TABS.get(department["slug"])
    if tabs is None:
        tabs = data.DEFAULT_DEPARTMENT_TABS

    # Every default string reads "the Department of {department}", and every
    # name in DEPARTMENTS begins with "Department Of", so substituting the
    # whole name gives "the Department of Department Of Physics". The
    # placeholder takes the SUBJECT instead - "Physics" - which is what those
    # sentences are written around. A name that does not carry the prefix is
    # used as it stands.
    subject = re.sub(r"^\s*department\s+(of\s+)?", "", department["name"],
                     flags=re.IGNORECASE).strip() or department["name"]

    def fill(value):
        return value.replace("{department}", subject) if value else value

    panels = []
    for index, row in enumerate(tabs):
        tab = dict(row)
        tab["slug"] = row.get("slug") or slugify(row["title"]) or "tab-%d" % (index + 1)
        tab["heading"] = fill(row.get("heading") or row["title"])
        tab["intro"] = fill(row.get("intro", ""))
        tab["body"] = [fill(p) for p in row.get("body", [])]
        tab["points"] = [{"label": fill(p.get("label", "")), "text": fill(p.get("text", ""))}
                         for p in row.get("points", [])]
        tab["icon"] = row.get("icon") or "book"
        # Message Desk sets 'image' in data.py and the panel lays the text out
        # beside it; a tab without one keeps the full width.
        tab["image"] = _asset(row.get("image", ""))
        # A heading inside the prose, under the Name/Designation lines - the
        # "Welcome to the Department of ..." line on a Message Desk tab.
        tab["subheading"] = fill(row.get("subheading", ""))
        # Whoever the message is from, printed as "Name:" / "Designation:"
        # above it. Optional: without it the message simply starts.
        person = row.get("person")
        if person:
            tab["person"] = {k: fill(v) for k, v in person.items()}
        # The signature carries {department} as well, so the shared default
        # block signs off as this department rather than as a placeholder.
        signature = row.get("signature")
        if signature:
            tab["signature"] = {k: fill(v) for k, v in signature.items()}
        panels.append(tab)
    return panels


# The Download Syllabus button rides on this tab, because a candidate who has
# just read what they need in order to apply is the one who wants to see what
# they would actually study. Matched on the slug, which slugify() derives from
# the tab title, so a course with its own COURSE_TABS entry gets the button
# too as long as it calls the tab Course Eligibility.
SYLLABUS_TAB_SLUG = "course-eligibility"


def _course_tabs(course):
    """Tab panels for a course page.

    Every course page carries the SAME three tabs, so they all read alike:
    Programme Overview, Course Eligibility, Career Opportunities. COURSE_TABS
    in data.py overrides the lot for a course that has been written up
    properly; without an entry there the three are built from the fields every
    course already has - description, eligibility and careers - so a course is
    a finished page the moment it is added to COURSES.

    A tab whose source field is empty is dropped rather than rendered as an
    empty panel, which is the one case where a page can still come up short.
    """
    rows = data.COURSE_TABS.get(course["slug"])
    if rows is None:
        rows = []
        if course.get("description"):
            rows.append({"title": "Programme Overview", "icon": "book",
                         "body": [course["description"]]})
        if course.get("eligibility"):
            # intro + points rather than a paragraph, so this tab is laid out
            # the same way as Programme Overview beside it.
            rows.append({"title": "Course Eligibility", "icon": "scales",
                         "intro": "Who can apply for %s:" % course["name"],
                         "points": [{"text": course["eligibility"]}]})
        if course.get("careers"):
            rows.append({"title": "Career Opportunities", "icon": "industry",
                         "layout": "slider",
                         "intro": "Roles this programme leads into:",
                         "points": [{"text": role} for role in course["careers"]]})

    panels = []
    for index, row in enumerate(rows):
        tab = dict(row)
        tab["slug"] = row.get("slug") or slugify(row["title"]) or "tab-%d" % (index + 1)
        tab["heading"] = row.get("heading") or row["title"]
        tab["intro"] = row.get("intro", "")
        tab["body"] = list(row.get("body", []))
        tab["points"] = [{"label": p.get("label", ""), "text": p.get("text", "")}
                         for p in row.get("points", [])]
        tab["icon"] = row.get("icon") or "book"

        # A tab marked 'slider' shows its points as a looping row of cards
        # rather than a list, each with a picture from CAREER_IMAGES. The
        # lookup is by the role's own wording, so one picture serves every
        # course that lists that role.
        tab["layout"] = row.get("layout", "")
        if tab["layout"] == "slider":
            tab["slides"] = [
                {"name": point["text"],
                 "image": _asset(data.CAREER_IMAGES.get(point["text"], ""))}
                for point in tab["points"] if point.get("text")
            ]

        # No PDF, no button - rather than a button that leads to a 404.
        tab["download"] = ""
        if tab["slug"] == SYLLABUS_TAB_SLUG and course.get("syllabus_url"):
            tab["download"] = {"url": course["syllabus_url"],
                               "label": "Download Syllabus"}

        panels.append(tab)
    return panels


def _course_faqs(course):
    """Questions for a course page.

    COURSE_FAQS in data.py holds the written-out ones. Without an entry the
    answers are assembled from that course's own record - eligibility,
    duration, intake, department, careers - so every course page carries the
    section and nothing in it is invented: each answer restates a field that
    is already on the page or in COURSES.
    """
    rows = data.COURSE_FAQS.get(course["slug"])
    if rows is not None:
        return rows

    name = course["name"]
    faqs = []

    if course.get("eligibility"):
        faqs.append({
            "question": "Who is eligible to apply for %s?" % name,
            "answer": course["eligibility"],
        })

    if course.get("duration"):
        answer = "%s runs for %s." % (name, course["duration"])
        if course.get("total_seats"):
            answer += (" The approved intake is %s seats for each admission "
                       "cycle." % course["total_seats"])
        faqs.append({
            "question": "How long is %s, and how many seats are there?" % name,
            "answer": answer,
        })

    if course.get("department_name"):
        answer = "%s is taught by the %s" % (name, course["department_name"])
        answer += (", part of the %s." % course["school_name"]
                   if course.get("school_name") else ".")
        faqs.append({
            "question": "Which department runs %s?" % name,
            "answer": answer,
        })

    if course.get("careers"):
        faqs.append({
            "question": "What roles can a %s graduate apply for?" % name,
            "answer": "Graduates go into roles such as %s."
                      % _readable_list(course["careers"]),
        })

    return faqs


def _readable_list(items):
    """'a, b and c' — for an answer sentence built out of a list field."""
    items = [str(i) for i in items if i]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return "%s and %s" % (", ".join(items[:-1]), items[-1])


def _course_board(course):
    """Board of Studies for a course page.

    COURSE_BOARD_OF_STUDIES names a board for one course; anything without an
    entry there falls back to the shared DEFAULT_COURSE_BOARD, so every course
    page carries the section rather than only the ones written up by hand.

    "{department}" is swapped for the course's own department, which is what
    lets a single shared board read correctly on all of them.
    """
    rows = data.COURSE_BOARD_OF_STUDIES.get(course["slug"])
    if rows is None:
        rows = data.DEFAULT_COURSE_BOARD

    department = course.get("department_name") or "the department"

    def fill(value):
        return value.replace("{department}", department) if value else value

    members = []
    for row in rows:
        member = dict(row)
        member["name"] = fill(row.get("name", ""))
        member["designation"] = fill(row.get("designation", ""))
        member["affiliation"] = fill(row.get("affiliation", ""))
        member["photo"] = _asset(row.get("photo"))
        members.append(member)
    return members


def _recruiters():
    """Logos for the recruiter panel, with their image paths resolved."""
    items = []
    for row in data.PARTNERS:
        item = dict(row)
        item["logo"] = _asset(row.get("logo"))
        if item["logo"]:
            items.append(item)
    return items


def department_list(request):
    """Every department, grouped under the school it belongs to."""
    groups = []
    for school in _schools():
        departments = _departments(school=school["slug"])
        if departments:
            groups.append({"school": school, "departments": departments})

    return render(request, "pages/department_list.html", {
        "groups": groups,
        "hero_title": "Departments",
        "hero_subtitle": "Every department of the university, listed under its school.",
        # The banner photograph, laid over the dark ground at low opacity by
        # page_hero.html so the white title stays readable. Swap the file name
        # here and that is the whole edit.
        "hero_image": "img/about/team.png",
        "crumbs": [{"label": "Academics"}, {"label": "Departments"}],
    })


def department_detail(request, slug):
    department = _find(_departments(), slug)
    if not department:
        return error_404(request, None)

    school = _find(data.SCHOOLS, department["school"])
    courses = [c for c in _courses() if c["department"] == slug]

    return render(request, "pages/department_detail.html", {
        "department": department,
        "school": school,
        "courses": courses,
        "faculty": _faculty(slug),
        "tabs": _department_tabs(department),
        "siblings": [d for d in _departments(school=department["school"])
                     if d["slug"] != slug],
        "hero_title": department["name"],
        "hero_subtitle": department["short_description"],
        "hero_image": school["card_image"] if school else "",
        "crumbs": [
            {"label": "Academics"},
            {"label": "Our Schools", "url": reverse("website:school_list")},
            {"label": department["school_name"], "url": department["school_url"]},
            {"label": department["name"]},
        ],
    })


def course_list(request):
    courses = _courses()
    selected_school = request.GET.get("school", "")
    selected_department = request.GET.get("department", "")
    selected_program = request.GET.get("program", "")

    # Picking a department implies its school, so a stale school in the query
    # string never fights with it.
    if selected_department:
        parent = _find(data.DEPARTMENTS, selected_department)
        if not parent:
            selected_department = ""
        else:
            selected_school = parent["school"]

    if selected_school:
        courses = [c for c in courses if c["school"] == selected_school]
    if selected_department:
        courses = [c for c in courses if c["department"] == selected_department]
    if selected_program:
        courses = [c for c in courses if c["program"] == selected_program]

    # Only offer department chips for the school in view; the full list of
    # seventeen would swamp the filter row.
    departments = _departments(school=selected_school) if selected_school else []

    return render(request, "pages/course_list.html", {
        "courses": courses,
        "schools": data.SCHOOLS,
        "departments": departments,
        "programs": data.PROGRAMS,
        "selected_school": selected_school,
        "selected_department": selected_department,
        "selected_program": selected_program,
        "hero_title": "Schools & Courses",
        "hero_subtitle": "Undergraduate, postgraduate, diploma and doctoral programmes "
                         "offered across the university.",
        "crumbs": [{"label": "Academics"}, {"label": "Schools & Courses"}],
    })


def course_detail(request, slug):
    course = _find(_courses(), slug)
    if not course:
        return error_404(request, None)

    # Nearest first: other courses of the same department, then the rest of
    # the school if the department is a small one.
    others = [c for c in _courses() if c["slug"] != slug]
    related = [c for c in others if c["department"] == course["department"]]
    related += [c for c in others
                if c["school"] == course["school"]
                and c["department"] != course["department"]]

    context = {
        "course": course,
        "related": related[:6],
        "tabs": _course_tabs(course),
        "faqs": _course_faqs(course),
        "board": _course_board(course),
        "recruiters": _recruiters(),
        "hero_title": course["name"],
        "hero_subtitle": "%s  |  %s" % (course["program_name"], course["duration"]),
        "hero_image": course["hero_image"],
        "crumbs": [
            {"label": "Academics"},
            {"label": "Schools & Courses", "url": reverse("website:course_list")},
            {"label": course["name"]},
        ],
    }
    context.update(_enquiry_context())
    return render(request, "pages/course_detail.html", context)


def facility_list(request):
    return render(request, "pages/facility_list.html", {
        "facilities": data.FACILITIES,
        "hero_title": "SVU Facilities",
        "hero_subtitle": "One of the best-in-class infrastructures on campus, built around "
                         "how students actually study, train and unwind.",
        "crumbs": [{"label": "Campus Life"}, {"label": "SVU Facilities"}],
    })


def partner_list(request):
    return render(request, "pages/partner_list.html", {
        "partners": data.PARTNERS,
        "hero_title": "Industry Partners",
        "hero_subtitle": "Organisations that work with us on curriculum, training, "
                         "internships and placement.",
        "crumbs": [{"label": "Centre"}, {"label": "Industry Collaboration"}],
    })


# ---------------------------------------------------------------- admission
def admission(request):
    context = {
        "steps": data.ADMISSION_STEPS,
        "scholarships": data.SCHOLARSHIPS,
        "programs": data.PROGRAMS,
        "featured_courses": [c for c in _courses() if c["is_featured"]],
        "hero_title": "Admission",
        "hero_subtitle": data.SITE["admission_banner_text"],
        "crumbs": [{"label": "Admission"}],
    }
    context.update(_enquiry_context())
    return render(request, "pages/admission.html", context)


def apply_online(request):
    """Full-page enquiry form. Handles both a normal POST and the AJAX POST."""
    if request.method == "POST":
        return enquiry_submit(request)

    context = {
        "hero_title": "Apply Online",
        "hero_subtitle": "Fill in the form and our admission team will call you back.",
        "crumbs": [
            {"label": "Admission", "url": reverse("website:admission")},
            {"label": "Apply Online"},
        ],
    }
    context.update(_enquiry_context())
    return render(request, "pages/apply.html", context)


@require_POST
def enquiry_submit(request):
    """Validate an enquiry.

    Nothing is stored yet — the submission is logged so the flow can be tested
    end to end.  Persisting it is a one-line change once the model exists.
    """
    form = EnquiryForm(request.POST)
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if form.is_valid():
        logger.info("Enquiry received: %s", {
            k: v for k, v in form.cleaned_data.items()
            if k not in ("captcha", "captcha_token", "company")
        })
        message = ("Thank you! Your enquiry has been received. "
                   "Our admission team will contact you shortly.")
        if is_ajax:
            return JsonResponse({"ok": True, "message": message})
        context = {
            "hero_title": "Thank you",
            "hero_subtitle": message,
            "crumbs": [
                {"label": "Admission", "url": reverse("website:admission")},
                {"label": "Thank you"},
            ],
        }
        context.update(_enquiry_context())
        return render(request, "pages/enquiry_thanks.html", context)

    if is_ajax:
        token, image = captcha.issue()
        return JsonResponse(
            {"ok": False, "errors": form.errors.get_json_data(),
             "captcha_token": token, "captcha_image": image},
            status=400,
        )

    context = {
        "hero_title": "Apply Online",
        "hero_subtitle": "Please correct the highlighted fields.",
        "crumbs": [
            {"label": "Admission", "url": reverse("website:admission")},
            {"label": "Apply Online"},
        ],
    }
    context.update(_enquiry_context(form))
    return render(request, "pages/apply.html", context)


# ---------------------------------------------------------------- events
def event_list(request):
    return render(request, "pages/event_list.html", {
        "page_obj": _paginate(request, _events()),
        "hero_title": "Events",
        "hero_subtitle": "Seminars, collaborations, celebrations and academic programmes "
                         "from across the campus.",
        "crumbs": [{"label": "Events"}],
    })


def event_detail(request, slug):
    events = _events()
    event = _find(events, slug)
    if not event:
        return error_404(request, None)

    return render(request, "pages/event_detail.html", {
        "event": event,
        "related": [e for e in events if e["slug"] != slug][:3],
        "hero_title": "Events",
        "crumbs": [
            {"label": "Events", "url": reverse("website:event_list")},
            {"label": event["title"][:60]},
        ],
    })


def notice_redirect(request, slug=None):
    """Old per-notice addresses land on the board.

    RedirectView cannot cover this one. It forwards whatever the pattern
    captured to reverse(), and notice_list takes no arguments, so the slug
    makes it raise NoReverseMatch and the redirect 500s instead of redirecting.
    Swallowing the slug here is the whole job.
    """
    return redirect("website:notice_list", permanent=True)


def notice_list(request):
    """The notice board page, written by hand in its template.

    Deliberately not built from NOTICES. That list still feeds the board on the
    home page; this page is maintained directly in
    ``templates/pages/notice_list.html`` so a notice can be laid out however it
    needs to be rather than squeezed into one shape.
    """
    # No context: the banner, its background image and every card are written
    # into the template, which is the point of the page being hand-held.
    return render(request, "pages/notice_list.html")


def about(request):
    """About Us — a bespoke page, so it gets its own template rather than the
    generic editorial one. The markup lives in ``templates/pages/about.html``.
    """
    return render(request, "pages/about.html")


def our_team(request):
    """Leadership and administration, one scroll-stacked panel per person."""
    # No stack_title/stack_lead here on purpose: the page's photo banner
    # carries that heading, so the include skips its own intro band.
    return render(request, "pages/our_team.html", {
        "team": data.TEAM,
        "stack_label": "The people behind %s" % data.SITE["site_name"],
    })


def our_mentors(request):
    """Mentors and advisors, using the same stacked panels as the team page."""
    # As on Our Team, no stack_title/stack_lead: the page's photo banner
    # carries that heading, so the include skips its own intro band.
    return render(request, "pages/our_mentors.html", {
        "mentors": data.MENTORS,
        "stack_label": "Mentors and advisors",
    })


def chancellors_message(request):
    """The full message, with the portrait beside it.

    Content is the CHANCELLOR dict in data.py — the same one the homepage
    band reads, so the excerpt and the message never drift apart.
    """
    chancellor = getattr(data, "CHANCELLOR", None)
    if not chancellor:
        return error_404(request, None)

    return render(request, "pages/chancellors_message.html",
                  {"chancellor": chancellor})


def training_placements(request):
    """The Training & Placement Cell.

    Written entirely by hand in the template - the wording, the figures, the
    placed students and the partner list are all there, so nothing about this
    page is edited here. The partner logos used to come from PARTNERS; they
    are named in the template now because the panel lists two dozen companies
    and only a handful have a logo file, and a row that names its partner is
    more use than one that hides it.

    No hero_subtitle: the design has the banner carrying the title alone.
    """
    return render(request, "pages/training_placements.html", {
        "hero_title": "Our Placements",
        "hero_image": "img/about/campus.jpg",
        "crumbs": [{"label": "Training & Placements"}],
    })


def infrastructure(request):
    """The campus: six tabs of photographs, then the conference band.

    Written by hand in the template, photographs and all - there is no data.py
    list behind it. No hero_subtitle: the design has the banner carrying the
    title on its own.
    """
    return render(request, "pages/infrastructure.html", {
        "hero_title": "Infrastructure",
        "hero_image": "img/facilities/garden.jpg",
        "crumbs": [{"label": "Infrastructure"}],
    })


def list_of_holidays(request):
    """The holiday list, sorted, with the weekday worked out from the date.

    The weekday is derived rather than stored so the two can never disagree:
    change a date in HOLIDAYS and the day beside it changes with it. A date
    that has already passed is flagged rather than dropped, so the list still
    reads as a full year.
    """
    today = datetime.date.today()
    rows = []
    for row in data.HOLIDAYS:
        try:
            day = datetime.datetime.strptime(row["date"], "%Y-%m-%d").date()
        except (KeyError, ValueError):
            # A malformed date costs that one row, not the page.
            logger.warning("HOLIDAYS: unreadable date %r", row.get("date"))
            continue
        rows.append({
            "date": day,
            "weekday": day.strftime("%A"),
            "occasion": row.get("occasion", ""),
            "note": row.get("note", ""),
            "is_past": day < today,
        })
    rows.sort(key=lambda r: r["date"])

    return render(request, "pages/list_of_holidays.html", {
        "holidays": rows,
        "upcoming": [r for r in rows if not r["is_past"]],
        "year": rows[0]["date"].year if rows else today.year,
        "hero_title": "List of Holidays",
        "hero_subtitle": "Days the university is closed.",
        "hero_image": "img/about/team.png",
        "crumbs": [{"label": "Academic"}, {"label": "List of Holidays"}],
    })


def academic_activities(request):
    """Conferences, workshops, lectures, FDPs and the industry interface.

    Takes no list of its own. Every item is one ``{% include %}`` line in
    ``templates/pages/academic_activities.html``, so adding one, rewording it
    or moving it between the five panels is an edit to that file alone.

    ACADEMIC_ACTIVITIES in data.py fed the card grid this page used to be and
    is no longer read here. It is left in place rather than deleted: the
    sentences in it are the source of the copy that now opens each panel.
    """
    return render(request, "pages/academic_activities.html", {
        "hero_title": "Academic Activities",
        "hero_subtitle": "Seminars, workshops, projects and collaborations that "
                         "run alongside the syllabus.",
        "hero_image": "img/about/campus.jpg",
        "crumbs": [{"label": "Academic"}, {"label": "Academic Activities"}],
    })


def academic_calendar(request):
    """Academic Calendar — every date lives in the template, not here.

    Edit ``templates/pages/academic_calendar.html`` to change the schedule.
    """
    return render(request, "pages/academic_calendar.html")


# The twelve months and the years the Newsletter page offers. A calendar
# rather than content, which is why it is here and not repeated on each of the
# twenty department lines in the template. Add a year and every department
# gains it; the PDFs are then read from
# static/documents/newsletter/<slug>/<year>-<month>.pdf
NEWSLETTER_YEARS = ["2024", "2025"]
NEWSLETTER_MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def public_self_disclosure(request):
    """Mandatory Disclosure — ten sections of rows, all in the template.

    Takes no context on purpose. Each row is one ``{% include %}`` line in
    ``templates/pages/public_self_disclosure.html`` carrying its label and
    whatever the link should open — a page on this site, a PDF or an outside
    address, all in the same slot.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/public_self_disclosure.html")


def vivek_jyoti_samman(request):
    """Vivek Jyoti Samman — the honourees, each with their film.

    Takes no context on purpose. Each person is one ``{% include %}`` line in
    ``templates/pages/vivek_jyoti_samman.html``, carrying their name, what
    they do, their portrait and the YouTube address Watch Now opens.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/vivek_jyoti_samman.html")


def university_press(request):
    """University Press — five panels, all in the template.

    Takes no context on purpose. Mission, Vision and Objectives are a numbered
    chip over its paragraph; Committee is a grid of name cards; Published
    Bookes is one ``{% include %}`` line per title. All of it is markup in
    ``templates/pages/university_press.html``.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/university_press.html")


def research_publication_cell(request):
    """Research And Publication Cell — four panels, all in the template.

    Takes no context on purpose. Mission, Vision and Objectives are a numbered
    chip over its paragraph, repeated; Activity is a department, its categories
    of output and their citations. All of it is markup in
    ``templates/pages/research_publication_cell.html``.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/research_publication_cell.html")


def research_funding(request):
    """Research Funding — the agencies open to research proposals.

    Takes no context on purpose. The three cards are markup in
    ``templates/pages/research_funding.html`` and every agency inside the
    first is one ``{% include %}`` line, so adding one is a line in that file
    and nothing else.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/research_funding.html")


def social_outreach(request):
    """Social Outreach Activity — the intro, the two panels and the camps.

    Takes no context on purpose. Every word is markup in
    ``templates/pages/social_outreach.html``: Mission and Vision are the same
    panel in two colours, and each activity is a block carrying its own report
    behind Read More.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/social_outreach.html")


def regulations(request):
    """Regulations — one row per regulation, each opening its document.

    Takes no context on purpose. Each regulation is one ``{% include %}`` line
    in ``templates/pages/regulations.html``, carrying its title and whatever
    Click To View should open.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/regulations.html")


def project(request):
    """Project — the funded schemes, each row opening its document.

    Takes no context on purpose. Each project is one ``{% include %}`` line in
    ``templates/pages/project.html``, carrying its title and whatever Click to
    View should open.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/project.html")


def publication(request):
    """Publication — a department bar that opens its faculty.

    Takes no context on purpose. Every department is a block of markup in
    ``templates/pages/publication.html`` and every faculty member is one
    ``{% include %}`` line inside it, so adding a name is a line in that file
    and nothing else.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/publication.html")


def newsletter(request):
    """Newsletter — a department opens its years, a year opens its months.

    The departments are twenty ``{% include %}`` lines in
    ``templates/pages/newsletter.html``; everything below one of them is built
    from the two lists above, so none of the 480 month rows is typed.
    """
    return render(request, "pages/newsletter.html", {
        "years": NEWSLETTER_YEARS,
        "months": NEWSLETTER_MONTHS,
    })


def incubation_centre(request):
    """Centre Of Incubation — one column of writing, all in the template.

    Takes no context on purpose. The whole page is markup in
    ``templates/pages/incubation_centre.html``, built from five repeating
    blocks, so any of it can be reworded without touching Python.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/incubation_centre.html")


def journal_list(request):
    """List of Journals — each row an anchor to that journal's own site.

    Takes no context on purpose. Each journal is one ``{% include %}`` line in
    ``templates/pages/journal_list.html``, carrying its title and its address,
    so adding one is a line in that file and nothing else.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/journal_list.html")


def iic(request):
    """Institution's Innovation Council — six panels, all in the template.

    Takes no context on purpose. The mission, the events, the newsletters, the
    members table and the Director's message are all markup in
    ``templates/pages/iic.html``, so any of them can be edited without
    touching Python.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/iic.html")


def e_resource(request):
    """E-Resource — the open access resources open to students and faculty.

    Takes no context on purpose. Each resource is one ``{% include %}`` line in
    ``templates/pages/e_resource.html``, carrying its title and whatever View
    More should open, so adding one is a line in that file and nothing else.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/e_resource.html")


def consultancy(request):
    """Consultancy — the policy, and the services each department offers.

    Takes no context on purpose. Every card is markup in
    ``templates/pages/consultancy.html``, each naming its own PDF, so adding a
    department or rewording the policy is an edit to that file alone.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/consultancy.html")


def collaboration(request):
    """Collaboration — academic, industry and healthcare partners.

    Takes no context on purpose. Each partner is one line in
    ``templates/pages/collaboration.html``, carrying its logo filename, its alt
    text and the name to show until the file is uploaded, so adding a partner
    is one line in that file and nothing else.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/collaboration.html")


def centre_skill_enhancement(request):
    """Centre For Skill Enhancement — the courses are written in the template.

    Takes no context on purpose. Each course is one block of markup in
    ``templates/pages/centre_skill_enhancement.html``, carrying its own
    syllabus behind Read More, so adding a course or rewording a unit is an
    edit to that file alone.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/centre_skill_enhancement.html")


def centre_faculty_development(request):
    """Centre For Faculty Development Programme — written in the template.

    Takes no context on purpose. All four panels — Mission, Vision, Objectives
    and the stack of reports — are markup in
    ``templates/pages/centre_faculty_development.html``, so rewording a point
    or adding a report is an edit to that file alone.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/centre_faculty_development.html")


def centre_of_excellence(request):
    """Centre For Excellence — the centres are written in the template.

    Takes no context on purpose. Each centre is one ``{% include %}`` line in
    ``templates/pages/centre_of_excellence.html``, so adding one, rewording it
    or reordering the list is an edit to that file alone. The schedule button
    under the list names its own PDF in the same file.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/centre_of_excellence.html")


def book_list(request):
    """List of Books — the departments are written in the template.

    Takes no context on purpose. Each department is one ``{% include %}`` line
    in ``templates/pages/book_list.html``, so adding one, rewording it or
    moving it between the University Publications and Others panels is an edit
    to that file alone.

    The two panels are separate lists rather than one list filtered twice: they
    do not hold the same departments, and a department can appear in both with
    a different list of books behind it.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/book_list.html")


def academic_patent_ipr(request):
    """Academic Patent & IPR — the inventions are written in the template.

    Takes no context on purpose. Each patent is one ``{% include %}`` line in
    ``templates/pages/academic_patent_ipr.html``, so adding one, rewording it
    or moving it between the Published and Grant panels is an edit to that file
    alone — no list here to keep in step with it.

    Its own template means its route has to sit above the generic
    ``page/<slug>/`` line in urls.py; below it, page_detail claims the URL
    first and renders an empty editorial placeholder.
    """
    return render(request, "pages/academic_patent_ipr.html")


def recognition_approvals(request):
    """Statutory approvals, each card linking a document."""
    return render(request, "pages/recognition_approvals.html",
                  {"recognitions": data.RECOGNITIONS})


def gallery(request):
    """Photo gallery — every photograph is named in the template.

    It has its own template rather than a PAGES entry, so its route has to sit
    above the generic ``page/<slug>/`` line in urls.py; below it, page_detail
    claims the URL first and renders an empty editorial placeholder.
    """
    return render(request, "pages/gallery.html")


def appreciations(request):
    """Appreciations — written by hand in its own template.

    Deliberately takes no context. APPRECIATIONS in data.py feeds the six-image
    slider on the home page; everything on this page is in the template, so a
    certificate can be given whatever caption or grouping it needs.
    """
    return render(request, "pages/appreciations.html")


def ugc_compliance(request):
    """UGC Compliance Documents — the cards come from UGC_DOCUMENTS in data.py.

    It has its own template rather than the generic editorial one, so its route
    has to sit above ``page/<slug>/`` in urls.py. The PAGES row of the same slug
    is left in place: the site search walks PAGES, and removing the row would
    make the page unsearchable.
    """
    return render(request, "pages/ugc_compliance.html",
                  {"ugc_documents": data.UGC_DOCUMENTS})


def life_detail(request, slug):
    """One Life at SVU page — Library, Laboratory, Classroom and the rest.

    Each has its own template under ``templates/pages/life/`` so the copy and
    the photographs on one can change without touching the other seven. This
    view only resolves the slug and hands over.

    The slug has to be one named in ``LIFE_AT_SVU``, so a mistyped URL is a 404
    rather than an attempt to render a template that is not there. A row added
    to data.py before its template exists is a 404 too, for the same reason a
    missing faculty file is no longer a 500: a gap in the content should cost
    that one page, not the request.
    """
    tile = _find(data.LIFE_AT_SVU, slug)
    if tile is None:
        raise Http404("No Life at SVU page called %r" % slug)

    try:
        return render(request, "pages/life/%s.html" % slug, {"tile": tile})
    except TemplateDoesNotExist:
        logger.warning("LIFE_AT_SVU lists %r but pages/life/%s.html is missing",
                       slug, slug)
        raise Http404("Life at SVU page %r has no template yet" % slug)


def brochure(request):
    """The brochure downloads.

    Each row is resolved through doc_url rather than a bare static tag. That
    filter hands back an empty string for a PDF that is not there instead of
    raising, which is what lets the page list a brochure before its file has
    been uploaded: the row renders, marked "Coming soon", and becomes a real
    download the moment the file is collected. A bare static tag would take
    the whole page down over one missing PDF.
    """
    items = []
    for row in data.BROCHURES:
        item = dict(row)
        item["href"] = row.get("url") or doc_url(row.get("file", ""))
        item["is_external"] = bool(row.get("url"))
        items.append(item)

    return render(request, "pages/brochure.html", {
        "brochures": items,
        "hero_title": "Brochure",
        "hero_subtitle": "Download the university prospectus and the brochure "
                         "for any school.",
        "crumbs": [{"label": "At a Glance"}, {"label": "Brochure"}],
    })


def page_detail(request, slug):
    """Render an editorial page.

    Pages that have not been written yet still resolve, using the label from the
    navigation, so no menu item ever leads to a dead end.
    """
    page = data.PAGES.get(slug)
    if page is None:
        title = _nav_title("/page/%s/" % slug) or slug.replace("-", " ").title()
        page = {
            "title": title,
            "subtitle": "",
            "content": "",
            "is_placeholder": True,
        }

    return render(request, "pages/page_detail.html", {
        "page": page,
        "hero_title": page["title"],
        "hero_subtitle": page.get("subtitle", ""),
        "crumbs": [{"label": page["title"]}],
    })


def faq(request):
    grouped = {}
    for item in data.FAQS:
        grouped.setdefault(item["category"], []).append(item)

    return render(request, "pages/faq.html", {
        "faq_groups": [{"category": k, "items": v} for k, v in grouped.items()],
        "hero_title": "Frequently Asked Questions",
        "hero_subtitle": "Answers to what applicants and students ask us most often.",
        "crumbs": [{"label": "FAQ"}],
    })


def contact(request):
    form = ContactForm(request.POST or None)
    sent = False
    if request.method == "POST" and form.is_valid():
        logger.info("Contact message received: %s", {
            k: v for k, v in form.cleaned_data.items() if k != "company"})
        sent = True
        form = ContactForm()

    return render(request, "pages/contact.html", {
        "form": form,
        "sent": sent,
        "hero_title": "Contact Us",
        "hero_subtitle": "Reach the admission helpline, the help desk or the campus office.",
        "crumbs": [{"label": "Contact Us"}],
    })


def search(request):
    query = (request.GET.get("q") or "").strip()
    results = []

    if query:
        needle = query.lower()

        def matches(*values):
            return any(needle in str(v or "").lower() for v in values)

        for school in _schools():
            if matches(school["name"], school["short_description"], school["description"]):
                results.append({"type": "School", "title": school["name"],
                                "url": school["url"],
                                "excerpt": school["short_description"]})
        for department in _departments():
            if matches(department["name"], department["short_description"]):
                results.append({"type": "Department", "title": department["name"],
                                "url": department["url"],
                                "excerpt": "%s  |  %s" % (department["school_name"],
                                                          department["short_description"])})
        for course in _courses():
            if matches(course["name"], course["eligibility"], course["school_name"],
                       course["department_name"]):
                results.append({"type": "Course", "title": course["name"],
                                "url": course["url"],
                                "excerpt": "%s  |  %s" % (course["department_name"],
                                                          course["duration"])})
        for event in _events():
            if matches(event["title"], event["excerpt"]):
                results.append({"type": "Event", "title": event["title"],
                                "url": event["url"], "excerpt": event["excerpt"]})
        for notice in _notices():
            if matches(notice["title"], notice["body"]):
                results.append({"type": "Notice", "title": notice["title"],
                                "url": notice["url"], "excerpt": notice["body"]})
        # About Us is not in PAGES (it has its own template), so it is indexed
        # here by hand rather than being silently unsearchable.
        about_blurb = ("Established in 2019 at Barrackpore, West Bengal. Affiliations, "
                       "recognitions, mission, core values and the awards won since "
                       "inception.")
        if matches("About Us About SVU", about_blurb):
            results.append({"type": "Page", "title": "About Us",
                            "url": reverse("website:about"),
                            "excerpt": about_blurb})

        # Same story for the Chancellor's Message — its text lives in
        # CHANCELLOR rather than PAGES, so index it by hand.
        chancellor = getattr(data, "CHANCELLOR", None)
        if chancellor and matches("Chancellor's Message", chancellor.get("excerpt"),
                                  strip_tags(chancellor.get("full_message", ""))):
            results.append({"type": "Page", "title": "Chancellor's Message",
                            "url": reverse("website:chancellors_message"),
                            "excerpt": chancellor.get("excerpt", "")})

        # And the Gallery, for the same reason: its own template, not a PAGES row.
        gallery_blurb = ("Photographs of the Barrackpore campus and its facilities, "
                         "the festivals and fests of the academic year, Freshers' Day "
                         "and the awards won since inception.")
        if matches("Gallery photographs photos", gallery_blurb):
            results.append({"type": "Page", "title": "Gallery",
                            "url": reverse("website:gallery"),
                            "excerpt": gallery_blurb})

        for slug, page in data.PAGES.items():
            if matches(page["title"], page["content"]):
                results.append({"type": "Page", "title": page["title"],
                                "url": reverse("website:page_detail", args=[slug]),
                                "excerpt": page["subtitle"]})

    return render(request, "pages/search.html", {
        "query": query,
        "results": results,
        "hero_title": "Search",
        "hero_subtitle": ('%d result%s for "%s"' % (len(results),
                                                    "" if len(results) == 1 else "s", query))
        if query else "Type a keyword to search the website.",
        "crumbs": [{"label": "Search"}],
    })


# ---------------------------------------------------------------- JSON endpoints
@require_GET
def api_cities(request):
    """Cities for the selected state — drives the dependent dropdown."""
    state = request.GET.get("state", "")
    cities = data.CITIES.get(state, [])
    return JsonResponse({"results": [{"id": c, "name": c} for c in cities]})


@require_GET
def api_courses(request):
    """Courses for the selected programme and/or department.

    Either filter may be omitted, so the dropdown still fills in when the
    visitor has only chosen one of the two.
    """
    program = request.GET.get("program", "")
    department = request.GET.get("department", "")

    courses = [
        c for c in data.COURSES
        if (not program or c["program"] == program)
        and (not department or c["department"] == department)
    ]
    return JsonResponse({"results": [{"id": c["slug"], "name": c["name"]} for c in courses]})


@require_GET
def api_captcha(request):
    token, image = captcha.issue()
    return JsonResponse({"token": token, "image": image})


# ---------------------------------------------------------------- errors
def error_404(request, exception=None):
    return render(request, "pages/404.html", {
        "hero_title": "Page not found",
        "crumbs": [{"label": "Not found"}],
    }, status=404)


def error_500(request):
    return render(request, "pages/500.html", status=500)
