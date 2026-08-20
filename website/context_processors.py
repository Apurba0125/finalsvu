"""Content that every template needs: identity, navigation and the footer."""
from django.urls import reverse

from . import data


def _department_panel():
    """School -> department tree for the Programs > Departments flyout.

    Built from SCHOOLS and DEPARTMENTS rather than written out in MAIN_NAV, so
    adding a department in data.py puts it in the menu with no second edit and
    no chance of the two lists disagreeing.

    A school with no departments is left out: an empty column heading in the
    panel reads as something failing to load.
    """
    groups = []
    for school in data.SCHOOLS:
        items = [
            {"title": department["name"],
             "href": reverse("website:department_detail",
                             args=[department["slug"]]),
             "is_external": False}
            for department in data.DEPARTMENTS
            if department["school"] == school["slug"]
        ]
        if items:
            groups.append({
                "title": school["name"],
                "href": reverse("website:school_detail", args=[school["slug"]]),
                "items": items,
            })
    return groups


# A child of a MAIN_NAV entry opens a third level by naming one of these in
# its 'panel' key.  Add a builder here and a 'panel' there; nothing else needs
# to know about it.
PANEL_BUILDERS = {
    "departments": _department_panel,
}

# The tree is the same for every visitor and every request, so it is built
# once on first use rather than on each page.  Restarting the server picks up
# an edit to data.py, which is also what reloads the module itself.
_nav_cache = None


def _main_nav():
    global _nav_cache
    if _nav_cache is not None:
        return _nav_cache

    nav = []
    for entry in data.MAIN_NAV:
        entry = dict(entry)
        children = []
        for child in entry.get("children") or []:
            child = dict(child)
            builder = PANEL_BUILDERS.get(child.get("panel"))
            if builder:
                child["groups"] = builder()
            children.append(child)
        if children:
            entry["children"] = children
        nav.append(entry)

    _nav_cache = nav
    return nav


def site_context(request):
    return {
        "site": data.SITE,
        "social_links": data.SOCIAL_LINKS,
        "top_nav": data.TOP_NAV,
        "main_nav": _main_nav(),
        "footer_links": data.FOOTER_LINKS,
    }
