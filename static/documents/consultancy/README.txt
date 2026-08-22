PDFs for the Consultancy page (/page/consultancy/).

Each card in templates/pages/consultancy.html already names the file it is
looking for:

    documents/consultancy/regulation.pdf              -> View Regulation
    documents/consultancy/mechanical-engineering.pdf  -> Mechanical Engineering
    documents/consultancy/civil-engineering.pdf       -> Civil Engineering

Drop the PDF in here under that name and run:

    python manage.py collectstatic --noinput

The card turns from "Document to follow" into a link opening the PDF in a new
tab. No edit to the template.

To use a different filename, change it in that card's {% with %} line - it is
set there and nowhere else.
