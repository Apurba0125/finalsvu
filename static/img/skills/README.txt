Course logos for the Centre For Skill Enhancement page
(/page/centre-skill-enhancement/).

Drop the image here, then in templates/pages/centre_skill_enhancement.html
swap that card's <svg> line for:

    <img src="{{ "img/skills/<filename>.png"|doc_url }}" alt="">

and run:  python manage.py collectstatic --noinput

The slot is a 36px square either way and object-fit keeps a logo of any
proportion inside it without distorting. alt="" is correct: the course name is
already in the heading beside it.
