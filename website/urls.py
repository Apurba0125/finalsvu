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
    path("events/notices/<slug:slug>/",
         RedirectView.as_view(pattern_name="website:notice_detail", permanent=True)),

    path("events/<slug:slug>/", views.event_detail, name="event_detail"),

    # --- Notices ---
    # Their own path rather than under events/. A notice is not an event, and
    # sitting beneath that prefix put the word in every notice URL and in the
    # breadcrumb above every notice.
    path("notices/", views.notice_list, name="notice_list"),
    path("notices/<slug:slug>/", views.notice_detail, name="notice_detail"),

    # --- Editorial pages & help ---
    # About Us has its own template, so it is matched before the generic
    # page route below. Keeping the same URL means the menus need no change.
    path("page/about-svu/", views.about, name="about"),
    path("page/our-team/", views.our_team, name="our_team"),
    path("page/our-mentors/", views.our_mentors, name="our_mentors"),
    path("page/recognition-approvals/", views.recognition_approvals,
         name="recognition_approvals"),
    path("page/academic-calendar/", views.academic_calendar,
         name="academic_calendar"),
    path("page/chancellors-message/", views.chancellors_message,
         name="chancellors_message"),
    path("life-at-svu/<slug:slug>/", views.life_detail, name="life_detail"),
    path("page/ugc-compliance/", views.ugc_compliance, name="ugc_compliance"),
    path("page/gallery/", views.gallery, name="gallery"),
    path("page/<slug:slug>/", views.page_detail, name="page_detail"),
    path("contact/", views.contact, name="contact"),
    path("faq/", views.faq, name="faq"),
    path("search/", views.search, name="search"),

    # --- JSON endpoints used by the enquiry form ---
    path("api/cities/", views.api_cities, name="api_cities"),
    path("api/courses/", views.api_courses, name="api_courses"),
    path("api/captcha/", views.api_captcha, name="api_captcha"),
]
