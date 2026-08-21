Conference reports for Academic Activities (/page/academic-activities/).

Drop a PDF here, then name it on the conference line in
templates/pages/academic_activities.html:

    {% include "includes/activity_conference.html" with title="..." doc="documents/conferences/<filename>.pdf" %}

and run:  python manage.py collectstatic --noinput

The View Details button appears by itself once the file is in place. Until
then the row shows the conference with no button, rather than a button that
opens nothing.
