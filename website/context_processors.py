"""Content that every template needs: identity, navigation and the footer."""
from . import data


def site_context(request):
    return {
        "site": data.SITE,
        "social_links": data.SOCIAL_LINKS,
        "top_nav": data.TOP_NAV,
        "main_nav": data.MAIN_NAV,
        "footer_links": data.FOOTER_LINKS,
    }
