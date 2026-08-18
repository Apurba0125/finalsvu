"""Small presentation helpers used across the templates.

Registered as a template ``builtins`` in settings, so templates do not need to
``{% load %}`` this module.
"""
import re

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def split_heading(value, first_words=2):
    """Render a heading with the opening words dark and the remainder gold.

    ``"WELCOME TO SWAMI VIVEKANANDA UNIVERSITY"|split_heading:2`` becomes
    "WELCOME TO" in near-black followed by the rest in the brand gold, which is
    how every section title on the site is styled.
    """
    if not value:
        return ""
    words = str(value).split()
    try:
        first_words = int(first_words)
    except (TypeError, ValueError):
        first_words = 2

    head = " ".join(words[:first_words])
    tail = " ".join(words[first_words:])
    html = '<span class="h-dark">%s</span>' % escape(head)
    if tail:
        html += ' <span class="h-accent">%s</span>' % escape(tail)
    return mark_safe(html)


@register.filter
def tel_href(value):
    """'+91-7044086270' -> 'tel:+917044086270'."""
    if not value:
        return ""
    digits = re.sub(r"[^\d+]", "", str(value))
    return "tel:%s" % digits


@register.filter
def wa_href(value):
    """Phone number -> WhatsApp chat link."""
    digits = re.sub(r"\D", "", str(value or ""))
    if not digits:
        return ""
    if len(digits) == 10:
        digits = "91" + digits
    return "https://wa.me/%s" % digits


@register.simple_tag(takes_context=True)
def is_current(context, href):
    """Return the ``is-current`` class when the request is on/under ``href``."""
    request = context.get("request")
    if not request or not href:
        return ""
    path = request.path
    if href == "/":
        return "is-current" if path == "/" else ""
    return "is-current" if path == href or path.startswith(href) else ""


@register.filter
def field_type(field):
    """Widget class name, so the template can style selects differently."""
    return field.field.widget.__class__.__name__
