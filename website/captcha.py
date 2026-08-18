"""A tiny, stateless CAPTCHA.

There is no database and no session store in this build, so the expected answer
travels with the form inside a signed token.  ``django.core.signing`` makes the
token tamper-proof and ``max_age`` on load makes it expire.
"""
import base64
import random
import string

from django.core import signing

SALT = "svu.enquiry.captcha"
MAX_AGE = 60 * 30  # 30 minutes
LENGTH = 6

# Characters that are hard to confuse with one another.
ALPHABET = "abcdefghjkmnpqrstuvwxyz23456789"


def new_code():
    return "".join(random.choice(ALPHABET) for _ in range(LENGTH))


def make_token(code):
    return signing.dumps(code.lower(), salt=SALT)


def check(token, answer):
    """True when ``answer`` matches the code sealed inside ``token``."""
    if not token or not answer:
        return False
    try:
        expected = signing.loads(token, salt=SALT, max_age=MAX_AGE)
    except signing.BadSignature:
        return False
    return str(answer).strip().lower() == expected


def as_svg_data_uri(code):
    """Draw the code as an inline SVG, returned as a ``data:`` URI.

    Keeping the image inline means no extra request and no image library.
    """
    colours = ["#b8942e", "#2b2b2b", "#a4913c", "#6b6b6b", "#14463f"]
    width, height = 130, 46

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
        'viewBox="0 0 %d %d">' % (width, height, width, height),
        '<rect width="%d" height="%d" fill="#ffffff"/>' % (width, height),
    ]

    # Faint noise so the code is not trivially machine-readable.
    for _ in range(6):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        parts.append(
            '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1" '
            'opacity=".35"/>' % (x1, y1, x2, y2, random.choice(colours))
        )
    for _ in range(14):
        parts.append(
            '<circle cx="%d" cy="%d" r="%d" fill="%s" opacity=".30"/>'
            % (random.randint(0, width), random.randint(0, height),
               random.randint(2, 5), random.choice(colours))
        )

    step = (width - 20) / float(len(code))
    for index, char in enumerate(code):
        x = 12 + index * step
        y = 32 + random.randint(-4, 4)
        rotate = random.randint(-22, 22)
        parts.append(
            '<text x="%.1f" y="%d" font-family="Georgia,serif" font-size="24" '
            'font-weight="bold" fill="%s" transform="rotate(%d %.1f %d)">%s</text>'
            % (x, y, random.choice(colours), rotate, x, y, char)
        )

    parts.append("</svg>")
    svg = "".join(parts)
    encoded = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return "data:image/svg+xml;base64,%s" % encoded


def issue():
    """Return ``(token, data_uri)`` for a freshly generated code."""
    code = new_code()
    return make_token(code), as_svg_data_uri(code)
