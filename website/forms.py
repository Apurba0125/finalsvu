"""Forms for the enquiry and contact pages.

These are plain ``forms.Form`` classes — nothing is written to a database yet.
A valid submission is logged and echoed back to the visitor; wiring it to a
model or an email backend later only touches the view.
"""
from django import forms

from . import captcha, data


def _choices(pairs, placeholder):
    return [("", placeholder)] + list(pairs)


class EnquiryForm(forms.Form):
    """The gold "Enquiry Form" panel on the homepage and admission page."""

    name = forms.CharField(
        max_length=80,
        error_messages={"required": "Please enter your name."},
        widget=forms.TextInput(attrs={"placeholder": "Enter Name *", "autocomplete": "name"}),
    )
    email = forms.EmailField(
        max_length=120,
        error_messages={"required": "Please enter your email address.",
                        "invalid": "Enter a valid email address."},
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter Email Address *", "autocomplete": "email"}),
    )
    mobile = forms.RegexField(
        regex=r"^[6-9]\d{9}$",
        error_messages={"required": "Please enter your mobile number.",
                        "invalid": "Enter a valid 10-digit Indian mobile number."},
        widget=forms.TextInput(attrs={
            "placeholder": "Enter Mobile Number *", "inputmode": "numeric",
            "maxlength": "10", "autocomplete": "tel-national",
        }),
    )
    state = forms.ChoiceField(
        choices=(), error_messages={"required": "Please select your state."},
    )
    city = forms.ChoiceField(
        choices=(), required=False,
    )
    program = forms.ChoiceField(
        choices=(), error_messages={"required": "Please select a programme."},
    )
    # Department is asked before course, because it narrows the course list.
    department = forms.ChoiceField(
        choices=(), error_messages={"required": "Please select a department."},
    )
    course = forms.ChoiceField(
        choices=(), error_messages={"required": "Please select a course."},
    )
    captcha = forms.CharField(
        max_length=12,
        error_messages={"required": "Please type the characters shown."},
        widget=forms.TextInput(attrs={"placeholder": "Enter Captcha", "autocomplete": "off"}),
    )
    captcha_token = forms.CharField(widget=forms.HiddenInput, required=False)
    consent = forms.BooleanField(
        error_messages={"required": "Please tick the consent box to continue."},
    )
    # Honeypot — real visitors never see it, bots fill it in.
    company = forms.CharField(required=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["state"].choices = _choices(
            [(s, s) for s in data.STATES], "Select State *")
        # The full city list is accepted on POST; the browser narrows it by state.
        all_cities = sorted({c for names in data.CITIES.values() for c in names})
        self.fields["city"].choices = _choices([(c, c) for c in all_cities], "Select City *")
        self.fields["program"].choices = _choices(
            [(p["slug"], p["name"]) for p in data.PROGRAMS], "Select Programme *")
        # Departments are grouped under their school, so the dropdown reads
        # school -> department -> (course, in the field below).
        self.fields["department"].choices = _choices(
            [(school["name"],
              [(d["slug"], d["name"]) for d in data.DEPARTMENTS
               if d["school"] == school["slug"]])
             for school in data.SCHOOLS
             if any(d["school"] == school["slug"] for d in data.DEPARTMENTS)],
            "Select Department *")
        # The browser narrows this by programme and department; the full list is
        # accepted on POST so the form still works without JavaScript, grouped
        # by department so the hierarchy still shows without it.
        self.fields["course"].choices = _choices(
            [(department["name"],
              [(c["slug"], c["name"]) for c in data.COURSES
               if c["department"] == department["slug"]])
             for department in data.DEPARTMENTS
             if any(c["department"] == department["slug"] for c in data.COURSES)],
            "Select Course *")

    def clean_company(self):
        if self.cleaned_data.get("company"):
            raise forms.ValidationError("Submission rejected.")
        return ""

    def clean(self):
        cleaned = super().clean()

        token = cleaned.get("captcha_token")
        answer = cleaned.get("captcha")
        if answer and not captcha.check(token, answer):
            self.add_error("captcha", "The characters do not match. Please try again.")

        # The course must belong to the department that was chosen above it.
        department = cleaned.get("department")
        course_slug = cleaned.get("course")
        if department and course_slug:
            course = next((c for c in data.COURSES if c["slug"] == course_slug), None)
            if course and course["department"] != department:
                self.add_error(
                    "course", "That course is not offered by the selected department.")

        return cleaned


class ContactForm(forms.Form):
    """Help-desk form on the contact page."""

    name = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={"placeholder": "Your name *"}),
    )
    email = forms.EmailField(
        max_length=120,
        widget=forms.EmailInput(attrs={"placeholder": "Your email address *"}),
    )
    mobile = forms.RegexField(
        regex=r"^[6-9]\d{9}$", required=False,
        error_messages={"invalid": "Enter a valid 10-digit Indian mobile number."},
        widget=forms.TextInput(attrs={"placeholder": "Mobile number", "inputmode": "numeric",
                                      "maxlength": "10"}),
    )
    subject = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={"placeholder": "Subject *"}),
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={"placeholder": "How can we help? *", "rows": 6}),
    )
    company = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_company(self):
        if self.cleaned_data.get("company"):
            raise forms.ValidationError("Submission rejected.")
        return ""
