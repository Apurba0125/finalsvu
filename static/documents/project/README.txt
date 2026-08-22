Documents for the Project page (/page/project/).

Drop a PDF here, then name it on that project's line in
templates/pages/project.html:

    {% include "includes/project_row.html" with title="ICICI Foundation" doc="documents/project/icici-foundation.pdf" %}

and run:  python manage.py collectstatic --noinput

That row turns from "Document to follow" into a Click to View link opening the
PDF in a new tab. Nothing else in the template changes.

The same doc= slot also takes a full web address instead, for a scheme that
should go straight to its own page:

    doc="https://icssr.org/"

Nothing has to say which kind it is - a full address is passed straight
through, a bare path is resolved against static/.
