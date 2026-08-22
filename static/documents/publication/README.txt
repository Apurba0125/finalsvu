Faculty publication lists for /page/publication/.

Drop a PDF here, then name it on that person's line in
templates/pages/publication.html:

    {% include "includes/publication_person.html" with name="Dr. Tanmoy Sarkar" url="documents/publication/tanmoy-sarkar.pdf" %}

and run:  python manage.py collectstatic --noinput

That row turns from "To follow" into a View More link opening the PDF in a new
tab. Nothing else in the template changes.

The same url= slot also takes a full web address instead, for a member whose
publications live on a profile elsewhere:

    url="https://scholar.google.com/citations?user=..."

Nothing has to say which kind it is - a full address is passed straight
through, a bare path is resolved against static/.
