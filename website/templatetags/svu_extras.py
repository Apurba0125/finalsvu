"""Small presentation helpers used across the templates.

Registered as a template ``builtins`` in settings, so templates do not need to
``{% load %}`` this module.
"""
import logging
import re

from django import template
from django.conf import settings
from django.contrib.staticfiles import finders
from django.templatetags.static import static as static_url
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()
logger = logging.getLogger(__name__)


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
def course_heading(value):
    """A course name with the subject half in the accent colour.

    ``split_heading`` counts words from the front, which works for a fixed
    opening like "Department Of". Course names have no fixed opening and no
    fixed length - "LL.M", "Diploma in Computer Science & Technology",
    "Master of Computer Applications (MCA)" - so counting words there gives
    "& Technology" as often as it gives anything readable.

    This splits at the connector instead, keeping it with the dark half:

        "Diploma in Computer Science & Technology"
            -> "Diploma in" + "Computer Science & Technology"
        "Master of Computer Applications (MCA)"
            -> "Master of" + "Computer Applications (MCA)"

    A name with no connector ("LL.M") stays entirely dark rather than being
    cut at an arbitrary word.
    """
    if not value:
        return ""
    text = str(value)
    match = re.search(r"\s+(in|of)\s+", text, re.IGNORECASE)
    if not match:
        return mark_safe('<span class="h-dark">%s</span>' % escape(text))
    head = text[:match.end()].rstrip()
    tail = text[match.end():].strip()
    return mark_safe('<span class="h-dark">%s</span> <span class="h-accent">%s</span>'
                     % (escape(head), escape(tail)))


@register.filter
def field_type(field):
    """Widget class name, so the template can style selects differently."""
    return field.field.widget.__class__.__name__


@register.filter
def doc_url(path):
    """Resolve a static path, or return "" when the file is not there.

    ``{% static %}`` raises ValueError under the manifest storage for a path
    that was never collected, and that takes the whole page down. On a page
    where the document links are typed by hand - the notice board - it turns a
    filename typo, or a PDF that has not been uploaded yet, into an outage.

    This returns an empty string instead, so the template can hide the link and
    the rest of the page keeps working:

        {% with pdf="documents/exam.pdf"|doc_url %}
          {% if pdf %}<a href="{{ pdf }}">Read More</a>{% endif %}
        {% endwith %}

    Which also means the path can be written before the file exists: the link
    appears by itself once the PDF is uploaded and collectstatic has run.

    Under DEBUG there is no manifest to miss, so nothing raises and the check
    is a look through the staticfiles finders instead. Without that, a card
    naming a PDF nobody has uploaded yet would show a Read More in development
    that 404s, and hide itself in production - the one place the difference
    would go unnoticed until it shipped.

    A full URL or a rooted path is handed straight back, so a document hosted
    somewhere else works the same way.
    """
    if not path:
        return ""
    value = str(path)
    if value.startswith(("http://", "https://", "//", "/")):
        return value
    if settings.DEBUG and finders.find(value) is None:
        logger.warning("doc_url: no static file found for %r", value)
        return ""
    try:
        return static_url(value)
    except ValueError:
        logger.warning("doc_url: no static file collected for %r", value)
        return ""


@register.filter
def marquee_duration(items):
    """Seconds for one pass of the announcement strip.

    A fixed duration would mean the strip reads at a comfortable pace with one
    announcement on it and races with five, because the same time is spent
    covering a much longer line. Timing it from the total length instead keeps
    the reading speed roughly steady: another announcement makes the strip take
    longer rather than making all of them go faster.

    The ratio is the one the single warning ran at - about 0.18s per character
    - with a floor so a one-line strip does not whip past.
    """
    chars = 0
    for item in items or []:
        try:
            chars += len(str(item.get("text", "")))
        except AttributeError:      # a bare string in the list
            chars += len(str(item))
    return max(32, int(chars * 0.18))
