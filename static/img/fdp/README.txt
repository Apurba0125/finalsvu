Posters for the Centre For Faculty Development Programme page
(/page/centre-faculty-development/), Report tab.

Drop the image here, then name it in that report's <figure class="fdp-poster">
in templates/pages/centre_faculty_development.html:

    {% with poster="img/fdp/<filename>.jpg"|doc_url %}

and run:  python manage.py collectstatic --noinput

The poster appears by itself once the file is in place. Until then the report
shows a hatched placeholder of the same width, so the copy around it does not
reflow when the real image lands.
