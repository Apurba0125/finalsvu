PDFs for the E-Resource page (/page/e-resource/).

Drop a PDF here, then name it on that resource's line in
templates/pages/e_resource.html:

    {% include "includes/eres_card.html" with title="Jstor:" doc="documents/e-resource/jstor.pdf" %}

and run:  python manage.py collectstatic --noinput

That card turns from "Link to follow" into a View More link opening the PDF in
a new tab.

The same doc= slot also takes a full web address instead, for a resource that
should go straight to its own site:

    doc="https://www.jstor.org/"

Nothing has to say which kind it is - a full address is passed straight
through, a bare path is resolved against static/.
