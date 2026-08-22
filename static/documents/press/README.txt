Books published by the University Press (/page/university-press/).

Drop a PDF here, then name it on that book's line in
templates/pages/university_press.html:

    {% include "includes/press_book.html" with title="Biotech Miracles" doc="documents/press/biotech-miracles.pdf" %}

and run:  python manage.py collectstatic --noinput

That row turns from "To follow" into a Click to View link opening the PDF in a
new tab. Nothing else in the template changes.

The same doc= slot also takes a full web address, for a book hosted elsewhere.
Nothing has to say which kind it is - a full address is passed straight
through, a bare path is resolved against static/.
