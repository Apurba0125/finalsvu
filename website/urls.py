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

    # --- Events & notices (notices first: they must win over the event slug) ---
    path("events/", views.event_list, name="event_list"),
    path("events/notices/", views.notice_list, name="notice_list"),
    path("events/notices/<slug:slug>/", views.notice_detail, name="notice_detail"),
    path("events/<slug:slug>/", views.event_detail, name="event_detail"),

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
    path("page/<slug:slug>/", views.page_detail, name="page_detail"),
    path("contact/", views.contact, name="contact"),
    path("faq/", views.faq, name="faq"),
    path("search/", views.search, name="search"),

    # --- JSON endpoints used by the enquiry form ---
    path("api/cities/", views.api_cities, name="api_cities"),
    path("api/courses/", views.api_courses, name="api_courses"),
    path("api/captcha/", views.api_captcha, name="api_captcha"),
]
