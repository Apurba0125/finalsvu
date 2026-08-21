Documents for the Centre For Excellence page (/page/centre-of-excellence/).

THE SCHEDULE
Name the file schedule.pdf and drop it here. The black "View Schedule" button
under the list appears by itself once it is in place; until then that spot
reads "The schedule will be published shortly."

A WRITE-UP FOR ONE CENTRE
Drop the PDF here, then name it on that centre's line in
templates/pages/centre_of_excellence.html:

    {% include "includes/coe_row.html" with title="..." doc="documents/coe/<filename>.pdf" %}

That card's "Details to follow" turns into a Read More link.

After adding any file:  python manage.py collectstatic --noinput
