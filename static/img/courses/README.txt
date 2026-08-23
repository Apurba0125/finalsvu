Course pictures
===============

Drop a picture in here NAMED AFTER THE COURSE and it appears by itself. No
line to edit anywhere: the site looks in this folder for a file whose name
matches the course's slug, which is the last part of the course's web address.

    /academics/courses/b-tech-in-civil-engineering/
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^ this is the slug

    so the file is    b-tech-in-civil-engineering.jpg

.jpg, .jpeg, .png and .webp all work. The picture shows on the course's own
page and on its card everywhere the course is listed - the course list, the
department page, the school page, the home page - all from the one file.

WHAT MAKES A GOOD ONE
Landscape, around 800x600, showing the work the course is about: a laboratory,
a studio, a site visit, students at a bench. It is cropped to 4:3 on the card,
so keep the subject near the middle. Under about 300 KB, or the page is slow
on a phone.

WHAT IF THERE IS NO FILE
Nothing breaks. The card falls back to the department's picture, then the
school's, then a plain placeholder - so a course is never a hole on the page
while its photograph is still being taken.

OVERRIDING IT
A 'card_image' written on the course's own row in website/data.py beats a file
found by name here. Use that when the picture cannot be named after the course
- one picture shared by several courses, for instance.

AFTER ADDING FILES
On the live site run:  python manage.py collectstatic --no-input
The development server picks new files up on the next page reload.
