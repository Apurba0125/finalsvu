Documents for the Mandatory Disclosure page (/page/public-self-disclosure/).

Every row that is not already pointing at a page on this site already names
the PDF it is looking for, e.g.

    documents/disclosure/prospectus.pdf
    documents/disclosure/annual-accounts-2021-2022.pdf

Drop the file in here under that name and run:

    python manage.py collectstatic --noinput

That row turns from "to follow" into a Click to View link opening the PDF in a
new tab. Nothing in the template changes.

To use a different filename, change it in that row's doc= slot. The same slot
also takes a page on this site (doc="/page/about-svu/") or a full web address
- nothing has to say which kind it is.
