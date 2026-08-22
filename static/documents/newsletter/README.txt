Departmental newsletters for /page/newsletter/.

THE PATH IS WORKED OUT, NOT TYPED. Put each PDF at:

    static/documents/newsletter/<slug>/<year>-<month>.pdf

<slug>   the short name on that department's line in
         templates/pages/newsletter.html, e.g. civil-engineering
<year>   2024, 2025 ... whichever years the view offers
<month>  the month in lowercase: january, february ... december

So the January 2024 issue for Civil Engineering is:

    static/documents/newsletter/civil-engineering/2024-january.pdf

Then run:  python manage.py collectstatic --noinput

That month turns from "Not published" into a View link by itself. Nothing in
the template changes - the page is driven entirely by where the files sit.

A month with no file stays on the list as "Not published", so a year always
reads as a complete twelve.
