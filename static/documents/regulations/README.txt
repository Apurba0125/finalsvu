Regulations for /page/regulations/.

Drop a PDF here, then name it on that regulation's line in
templates/pages/regulations.html:

    {% include "includes/regulation_row.html" with title="M.Sc. Regulations" doc="documents/regulations/msc.pdf" %}

and run:  python manage.py collectstatic --noinput

That row turns from "Document to follow" into a Click To View link opening the
PDF in a new tab. Nothing else in the template changes.

The same doc= slot also takes a full web address, for a regulation hosted
elsewhere. Nothing has to say which kind it is - a full address is passed
straight through, a bare path is resolved against static/.
