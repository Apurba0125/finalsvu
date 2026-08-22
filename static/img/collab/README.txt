Partner logos for the Collaboration page (/page/collaboration/).

Each partner's line in templates/pages/collaboration.html already names the
file it is looking for, e.g.

    img/collab/fortis.png

Drop that file in here and run:

    python manage.py collectstatic --noinput

and the cell switches from the partner's name to its mark by itself. No edit
to the template.

PNG with a transparent background works best — the cells are white, and a logo
on its own white rectangle will show its edges. The cell is a 4:3 box and the
mark is scaled to fit inside it without cropping, so any proportion is fine
and nothing needs resizing first.
