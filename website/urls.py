"""URL map.

The paths here match the hrefs stored in ``data.py`` (navigation, quick links
and footer), so the menus resolve without any rewriting.
"""
from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),

    # --- Academics ---
    path("academics/", RedirectView.as_view(pattern_name="website:school_list"),
         name="academics"),
    path("academics/schools/", views.school_list, name="school_list"),
    path("academics/schools/<slug:slug>/", views.school_detail, name="school_detail"),
    path("academics/departments/", views.department_list, name="department_list"),
    path("academics/departments/<slug:slug>/", views.department_detail,
         name="department_detail"),
    path("academics/courses/", views.course_list, name="course_list"),
    path("academics/courses/<slug:slug>/", views.course_detail, name="course_detail"),
    path("academics/facilities/", views.facility_list, name="facility_list"),
    path("academics/industry-partners/", views.partner_list, name="partner_list"),

    # --- Admission ---
    path("admission/", views.admission, name="admission"),
    path("admission/apply/", views.apply_online, name="apply"),
    path("admission/enquiry/", views.enquiry_submit, name="enquiry_submit"),

    # --- Events ---
    path("events/", views.event_list, name="event_list"),

    # The old notice addresses, kept so anything already linking to them still
    # lands. They MUST come before events/<slug>/ for the same reason the
    # notices themselves used to: that pattern matches "notices" as an event
    # slug and 404s on it. RedirectView carries the captured slug through to
    # the named route, so the detail case needs no view of its own, and
    # permanent=True because this is a move rather than a detour.
    path("events/notices/",
         RedirectView.as_view(pattern_name="website:notice_list", permanent=True)),
    path("events/notices/<slug:slug>/", views.notice_redirect),

    path("events/<slug:slug>/", views.event_detail, name="event_detail"),

    # --- Notices ---
    # Their own path rather than under events/. A notice is not an event, and
    # sitting beneath that prefix put the word in every notice URL and in the
    # breadcrumb above every notice.
    path("notices/", views.notice_list, name="notice_list"),
    # There is no page per notice any more. The slug pattern is kept only so
    # links already pointing at one land on the board instead of a 404. It goes
    # through views.notice_redirect rather than RedirectView, which would hand
    # the captured slug to a route that takes none and raise NoReverseMatch.
    path("notices/<slug:slug>/", views.notice_redirect),

    # --- Editorial pages & help ---
    # About Us has its own template, so it is matched before the generic
    # page route below. Keeping the same URL means the menus need no change.
    path("page/about-svu/", views.about, name="about"),
    path("page/our-team/", views.our_team, name="our_team"),
    path("page/our-mentors/", views.our_mentors, name="our_mentors"),
    path("page/regulations/", views.regulations, name="regulations"),
    path("page/project/", views.project, name="project"),
    path("page/publication/", views.publication, name="publication"),
    path("page/newsletter/", views.newsletter, name="newsletter"),
    path("page/incubation-centre/", views.incubation_centre,
         name="incubation_centre"),
    path("page/journals/", views.journal_list, name="journal_list"),
    path("page/iic/", views.iic, name="iic"),
    path("page/e-resource/", views.e_resource, name="e_resource"),
    path("page/consultancy/", views.consultancy, name="consultancy"),
    path("page/collaboration/", views.collaboration, name="collaboration"),
    path("page/centre-skill-enhancement/", views.centre_skill_enhancement,
         name="centre_skill_enhancement"),
    path("page/centre-faculty-development/", views.centre_faculty_development,
         name="centre_faculty_development"),
    path("page/centre-of-excellence/", views.centre_of_excellence,
         name="centre_of_excellence"),
    path("page/book/", views.book_list, name="book_list"),
    path("page/academic-patent-ipr/", views.academic_patent_ipr,
         name="academic_patent_ipr"),
    path("page/recognition-approvals/", views.recognition_approvals,
         name="recognition_approvals"),
    path("page/academic-calendar/", views.academic_calendar,
         name="academic_calendar"),
    path("page/list-of-holidays/", views.list_of_holidays,
         name="list_of_holidays"),
    path("page/training-placements/", views.training_placements,
         name="training_placements"),
    path("page/infrastructure/", views.infrastructure, name="infrastructure"),
    path("page/academic-activities/", views.academic_activities,
         name="academic_activities"),
    path("page/chancellors-message/", views.chancellors_message,
         name="chancellors_message"),
    path("life-at-svu/<slug:slug>/", views.life_detail, name="life_detail"),
    path("page/appreciations/", views.appreciations, name="appreciations"),
    path("page/ugc-compliance/", views.ugc_compliance, name="ugc_compliance"),
    path("page/gallery/", views.gallery, name="gallery"),
    path("page/brochure/", views.brochure, name="brochure"),
    path("page/<slug:slug>/", views.page_detail, name="page_detail"),
    path("contact/", views.contact, name="contact"),
    path("faq/", views.faq, name="faq"),
    path("search/", views.search, name="search"),

    # --- JSON endpoints used by the enquiry form ---
    path("api/cities/", views.api_cities, name="api_cities"),
    path("api/courses/", views.api_courses, name="api_courses"),
    path("api/captcha/", views.api_captcha, name="api_captcha"),
]
