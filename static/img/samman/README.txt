Portraits for the Vivek Jyoti Samman page (/page/vivek-jyoti-samman/).

Each card in templates/pages/vivek_jyoti_samman.html already names the file it
is looking for, built from the person's name, e.g.

    img/samman/rupak-barua.jpg

Drop that file in here and run:

    python manage.py collectstatic --noinput

The hatched placeholder is replaced by the portrait. Until then the
placeholder holds the SAME SHAPE, so nothing on the page moves when the real
photograph lands.

Portraits are cropped to a 4:3 box from the TOP rather than the centre,
because a face sits in the upper half of a portrait far more often than the
middle - so any proportion of original works and nothing needs resizing first.
Change the ratio in static/css/samman.css and every card follows.
