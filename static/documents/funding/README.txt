Documents for the Research Funding page (/page/research-funding/).

The two lower cards already name the files they are looking for:

    documents/funding/indian-funding-agencies.pdf
    documents/funding/international-funding-agencies.pdf

Drop them in here and run:

    python manage.py collectstatic --noinput

Each card turns from "Document to follow" into a Click To View link opening
the PDF in a new tab.

An individual agency in the first card's list can also point at a PDF here,
by putting the path in its url= slot instead of a web address:

    url="documents/funding/dst.pdf"
