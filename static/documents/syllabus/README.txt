Course syllabus PDFs
====================

Drop a PDF in here NAMED AFTER THE COURSE and a "Download Syllabus" button
appears on that course's page, under the Course Eligibility tab. There is no
line to edit anywhere: the site looks in this folder for a file whose name
matches the course's slug, which is the last part of the course's web address.

    /academics/courses/diploma-in-computer-science-technology/
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ this is the slug

    so the file is    diploma-in-computer-science-technology.pdf

PDF only.

NO FILE, NO BUTTON
A course without a PDF here simply shows no button, rather than one that
leads to a 404. So this folder can be filled in a few courses at a time.

OVERRIDING IT
A 'syllabus' line written on the course's own row in website/data.py beats a
file found by name, and can point anywhere under static/ or at a full URL:

    'syllabus': 'documents/syllabus/btech-cse-2024-regulation.pdf',
    'syllabus': 'https://example.ac.in/syllabus.pdf',

Use that when the PDF cannot be named after the course - one syllabus shared
by several courses, or a file whose name carries the regulation year.

AFTER ADDING FILES
On the live site run:  python manage.py collectstatic --no-input
The development server picks new files up on the next page reload.
