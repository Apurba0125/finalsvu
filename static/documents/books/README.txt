Department book lists for the List of Books page (/page/book/).

Drop a PDF here, then name it on that department's line in
templates/pages/book_list.html:

    {% include "includes/book_row.html" with title="..." doc="documents/books/<filename>.pdf" %}

and run:  python manage.py collectstatic --noinput

The row turns into a link by itself once the file is in place. Until then it
shows the department with a faded arrow, rather than a link that opens
nothing.
