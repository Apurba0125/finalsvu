"""Single source of content for the whole front end.

Every page is rendered from the plain Python structures below - there is no
database and no admin panel yet.  ``website/views.py`` imports this module,
picks what a page needs and hands it to the template.  When the data layer
moves to models later, only ``views.py`` has to change.
"""

# --------------------------------------------------------------------------
# Global identity, contact details and calls to action
SITE = {'site_name': 'Swami Vivekananda University',
 'short_name': 'SVU',
 'tagline': 'Excellence. Innovation. Entrepreneurship',
 'logo': 'img/logo.jpeg',
 'address_line1': 'Telinipara, Barasat - Barrackpore Rd Bara Kanthalia West Bengal - 700121.',

 'phones': ['+91-7044086270', '+91-7980333922', '+91-9830278216', '+91-8961334184'],
#  'toll_free': '1800 121 8383',
#  'toll_free_hours': '10AM to 6PM',
 'email': 'info@swamivivekanandauniversity.ac.in',
 'website': 'https://www.swamivivekanandauniversity.ac.in',
 # Contact page: 'map_url' is the Get directions button, 'map_embed_url' the
 # map shown under the form.  Blank either one and that piece disappears.
 'map_url': 'https://www.google.com/maps/search/?api=1&query=Swami+Vivekananda+University+Barrackpore',
 'map_embed_url': 'https://www.google.com/maps?q=Swami+Vivekananda+University,+Telinipara,+Barasat+-+Barrackpore+Rd,+Bara+Kanthalia,+West+Bengal+700121&output=embed',
 'whatsapp_number': '7044086270',
 'whatsapp_url': 'https://wa.me/917044086270',
 # The scrolling gold strip under the header. Add, remove or reorder rows and
 # the strip follows; empty the list and the whole strip disappears.
 #
 #   'text'         what is read out. Required.
 #   'url'          where it goes when clicked. Leave '' for a plain
 #                  announcement that is not a link.
 #   'is_external'  True opens it in a new tab. Only for another site.
 #
 # The strip keeps a steady reading pace however many rows are on it - the
 # animation is timed from the total length, so adding a row makes the strip
 # take longer rather than making everything race past.
 'marquee_items': [
     {'text': 'Beware of fake agents/consultants!! SVU does not take admission through any '
              'agents/consultants. For any admission related query please refer to SVU '
              'website only.',
      'url': '',
      'is_external': False},

     {'text': 'Admissions open for the 2026-27 session - apply online.',
      'url': '/admission/apply/',
      'is_external': False},

     {'text': 'Notice: revised examination dates published on the notice board.',
      'url': '/notices/',
      'is_external': False},
 ],
 'admission_banner_text': 'ADMISSION OPEN 2026-27',
 'apply_now_url': '/admission/apply/',
 'pay_fee_url': 'https://www.swamivivekanandauniversity.ac.in/Pay-online/',
 'ugc_documents_url': '/page/ugc-compliance/',
 'welcome_heading': 'WELCOME TO SWAMI VIVEKANANDA UNIVERSITY',
 'welcome_text': 'Welcome to Swami Vivekananda University. We are an institution in West '
                 'Bengal dedicated to the pursuit of knowledge and excellence and providing '
                 'quality education to our students. Since our inception, we have been '
                 'striving to provide our students with an exceptional learning experience. '
                 'Our aim is to facilitate and nurture the growth and development of our '
                 'students and to ensure that they reach their full potential.\n'
                 'We offer a range of undergraduate, postgraduate and diploma courses in a '
                 'variety of subjects. These courses range from engineering and management to '
                 'humanities.\n'
                 '\n'
                 'Our courses are designed to provide students with the skills and expertise '
                 'required to excel in their chosen fields. Our faculty members are highly '
                 'experienced and qualified professionals who are committed to providing our '
                 'students with the best possible education.\n'
                 '\n'
                 'Our faculty members are experts in their respective fields and are '
                 'passionate about helping our students develop the knowledge and skills they '
                 'need to succeed. We strive to create a learning environment where our '
                 'students can grow and develop in a safe and supportive environment.',
 'admission_ad_image': 'img/branding/admission-ad.jpg',
 'facebook_page_url': 'https://www.facebook.com/SwamiVivekanandaUniversityOfficial',
 # The paragraph under the logo in the footer's first column.
 'footer_about': 'Swami Vivekananda University was established in the year 2019 by Swami '
                 'Vivekananda Group of Institutions (RERF) and over the last couple of years '
                 'has grown in rapid strides to transform it into a reputed University.',
 'copyright_text': 'Copyright © SVU. All Rights Reserved.',
 'designer_credit': '',
 'designer_url': '',
 'meta_description': 'Swami Vivekananda University — offering UG, PG and Ph.D programmes in '
                     'engineering, management, law, media, design, nursing and more.'}

# --------------------------------------------------------------------------
SOCIAL_LINKS = [{'platform': 'facebook',
  'label': 'Facebook',
  'url': 'https://www.facebook.com/SwamiVivekanandaUniversityOfficial'},
 {'platform': 'youtube',
  'label': 'Youtube',
  'url': 'https://www.youtube.com/@swamivivekanandauniversity-bkp/videos'},
 {'platform': 'instagram',
  'label': 'Instagram',
  'url': 'https://www.instagram.com/official_svu_barrackpore/'},
 {'platform': 'linkedin',
  'label': 'Linkedin',
  'url': 'https://www.linkedin.com/company/swami-vivekananda-university-kolkata/posts/?feedView=all'}]

# --------------------------------------------------------------------------
# Utility bar above the header
TOP_NAV = [{'title': 'FAQ', 'href': '/faq/', 'is_external': False},
 {'title': 'Help Desk', 'href': '/contact/', 'is_external': False}]

# --------------------------------------------------------------------------
# Yellow navigation bar, with dropdown children
MAIN_NAV = [{'title': 'About SVU',
  'href': '/page/about-svu/',
  'is_external': False,
  'children': [{'title': 'About Us', 'href': '/page/about-svu/', 'is_external': False},
               {'title': "Our team", 'href': '/page/our-team/', 'is_external': False},
               {'title': "Our Mentors", 'href': '/page/our-mentors/', 'is_external': False},
               {'title': "Recognition & Approvals", 'href': '/page/recognition-approvals/', 'is_external': False},
                ]},
 # 'panel' on a child opens a third level. The value names a builder in
 # website/context_processors.py, which fills the child's 'groups' at render
 # time - so nothing below is listed by hand and the menu cannot drift from
 # SCHOOLS and DEPARTMENTS. 'departments' groups every department under its
 # school; a child with no 'panel' stays an ordinary one-line link.
 {'title': 'Programs',
  'href': '/academics/schools/',
  'is_external': False,
  'children': [{'title': 'Our Schools', 'href': '/academics/schools/', 'is_external': False},
               {'title': 'Departments',
                'href': '/academics/departments/',
                'is_external': False,
                'panel': 'departments'}]},
               
              
 {'title': 'Academic',
  'href': '/admission/',
  'is_external': False,
  'children': [{'title': 'Academics Activity', 'href': '/page/academic-activities/', 'is_external': False},
               {'title': 'List of Holidays', 'href': '/page/list-of-holidays/', 'is_external': False},
               {'title': 'Library', 'href': 'https://svu.knimbus.com/portal/v2/default/home', 'is_external': True},
               {'title': 'Academic Calendar','href': '/page/academic-calendar/', 'is_external': False},
                ]},

 # Both pages are written by hand in their own templates rather than built
 # from a list here, so there are no children to add: the wording lives in
 # templates/pages/training_placements.html and .../infrastructure.html.
 {'title': 'Training & Placements',
  'href': '/page/training-placements/',
  'is_external': False,
  'children': []},

 {'title': 'Infrastructure',
  'href': '/page/infrastructure/',
  'is_external': False,
  'children': []},
 # 'columns': 3 turns this dropdown into the wide three-column panel.  Any
 # nav entry can use it; without the key the menu stays a single column.
 # Items fill the first column top to bottom, then the second, then the third,
 # so keep the list in the order you want to read down the columns.
 {'title': 'At a Glance',
  'href': '#',
  'is_external': False,
  'columns': 3,
  'children': [{'title': 'Academic Patent & IPR', 'href': '/page/academic-patent-ipr/', 'is_external': False},
               {'title': 'Academic Activities', 'href': '/page/academic-activities/', 'is_external': False},
               {'title': 'Appreciations', 'href': '/page/appreciations/', 'is_external': False},
               {'title': 'Annual Report', 'href': '/static/img/annual_report/Annual Report Draft 1.pdf', 'is_external': True},
               {'title': 'Book', 'href': '/page/book/', 'is_external': False},
               {'title': 'Brochure', 'href': '/page/brochure/', 'is_external': False},
               {'title': 'Building Plan', 'href': '/page/building-plan/', 'is_external': False},
               {'title': 'Centre For Excellence', 'href': '/page/centre-of-excellence/', 'is_external': False},
               {'title': 'Centre For Faculty Development Programme', 'href': '/page/centre-faculty-development/', 'is_external': False},

               {'title': 'Disclosure', 'href': '/page/public-self-disclosure/', 'is_external': False},
               {'title': 'Centre For Skill Enhancement', 'href': '/page/centre-skill-enhancement/', 'is_external': False},
               {'title': 'Collaboration', 'href': '/page/collaboration/', 'is_external': False},
               {'title': 'Consultancy', 'href': '/page/consultancy/', 'is_external': False},
               {'title': 'E-Resource', 'href': '/page/e-resource/', 'is_external': False},
               {'title': 'Gallery', 'href': '/page/gallery/', 'is_external': False},
               {'title': 'IIC', 'href': '/page/iic/', 'is_external': False},
               {'title': 'Journals', 'href': '/page/journals/', 'is_external': False},
               {'title': 'Incubation Centre', 'href': '/page/incubation-centre/', 'is_external': False},
            #    {'title': 'List of Funding Agencies', 'href': '/page/funding-agencies/', 'is_external': False},
               {'title': 'Newsletter', 'href': '/page/newsletter/', 'is_external': False},

               {'title': 'Publication', 'href': '/page/publication/', 'is_external': False},
               {'title': 'Project', 'href': '/page/project/', 'is_external': False},
               {'title': 'Regulations', 'href': '/page/regulations/', 'is_external': False},
               {'title': 'Research And Publication Cell', 'href': '/page/research-publication-cell/', 'is_external': False},
               {'title': 'Research Funding', 'href': '/page/research-funding/', 'is_external': False},
               {'title': 'Student Handbook', 'href': '/static/img/annual_report/StudentHandbookFinal.pdf', 'is_external': False},
               {'title': 'Social Outreach Activities', 'href': '/page/social-outreach-activities/', 'is_external': False},
               {'title': 'Testing Facilities', 'href': '/static/img/annual_report/Material Testing Facility at Swami Vivekananda University.pdf', 'is_external': False},
               {'title': 'University Press', 'href': '/page/university-press/', 'is_external': False},
               {'title': 'Vivek Jyoti Samman', 'href': '/page/vivek-jyoti-samman/', 'is_external': False}]},
 {'title': 'Events', 'href': '/events/', 'is_external': False, 'children': []},
#  {'title': 'IQAC',
#   'href': '/page/iqac/',
#   'is_external': False,
#   'children': [{'title': 'About IQAC', 'href': '/page/iqac/', 'is_external': False},
#                {'title': 'AQAR Reports', 'href': '/page/aqar-reports/', 'is_external': False},
#                {'title': 'Feedback', 'href': '/page/iqac-feedback/', 'is_external': False}]},
 {'title': 'Student Form',
  'href': '/page/student-forms/',
  'is_external': False,
  'children': []},
#  {'title': 'NIRF',
#   'href': '/page/nirf/',
#   'is_external': False,
#   'children': [{'title': 'NIRF 2026', 'href': '/page/nirf/', 'is_external': False},
#                {'title': 'Data Templates', 'href': '/page/nirf-data/', 'is_external': False}]},
 {'title': 'Centre',
  'href': '/page/centre-of-excellence/',
  'is_external': False,
  'children': [{'title': 'Centre for Innovation & Entrepreneurship',
                'href': '/page/centre-innovation/',
                'is_external': False},
               {'title': 'Centre of Excellence',
                'href': '/page/centre-of-excellence/',
                'is_external': False},
               {'title': 'Centre for Women Studies',
                'href': '/page/centre-women-studies/',
                'is_external': False},
               ]},

 {'title': 'Student Welfare Committees',
  'href': '/page/student-welfare/',
  'is_external': False,
  'children': [{'title': 'Anti-Ragging Committee',
                'href': '/page/anti-ragging/',
                'is_external': False},
               {'title': 'Internal Complaints Committee',
                'href': '/page/internal-complaints/',
                'is_external': False},
               {'title': 'Grievance Redressal',
                'href': '/page/grievance-redressal/',
                'is_external': False},
               {'title': 'SC/ST Committee',
                'href': '/page/sc-st-committee/',
                'is_external': False}]},

{'title': 'Career','href': '/page/career/','is_external': False,},


 {'title': 'Media',
  'href': '#',
  'is_external': False,
  'children': [{'title': 'Blogs','href': '/page/blogs/','is_external': False},
               {'title': 'Svu Podcast', 'href': '/page/svu-podcast/', 'is_external': False},
               ]},

{'title': 'UGC-2f','href': '#','is_external': False,},

{'title': 'Contact','href': '/contact/','is_external': False},



 # Full URL off to the main university site, so is_external is True — that is
 # what opens it in a new tab.  'children' must be present even when empty:
 # the menu and the page-title lookup both walk it.
 ]
# --------------------------------------------------------------------------
# The footer's link columns, left to right.  Add, remove or reorder a column
# here and the footer follows — the grid works out how many there are.
#
# The first two columns of the footer are NOT here: the brand blurb comes from
# SITE['footer_about'] and the contact column from SITE's address, phones and
# email, so those details are never written down twice.
#
# Two columns may share a title ("Our Links"), which is how a long list is
# split across two columns without one running much taller than the rest.
FOOTER_LINKS = [
 {'title': 'Admissions',
  'links': [{'title': 'Admission Process', 'url': '/admission/', 'is_external': False},
            {'title': 'Scholarships', 'url': '/page/scholarships/', 'is_external': False},
            {'title': 'Fee Structure', 'url': '/page/fee-structure/', 'is_external': False},
            {'title': 'FAQs', 'url': '/faq/', 'is_external': False},
            
            
            ]},

 {'title': 'Our Links',
  'links': [
      
             {'title': 'NPTEL Courses', 'url': 'https://nptel.ac.in/', 'is_external': True},
            {'title': 'NATS', 'url': 'https://nats.education.gov.in/', 'is_external': True},
            {'title': 'NDLI', 'url': 'https://ndl.iitkgp.ac.in/', 'is_external': True},
            {'title': 'e Sodh Ganga', 'url': 'https://shodhganga.inflibnet.ac.in/', 'is_external': True},
            {'title': 'e-PGPathshala', 'url': 'https://epgp.inflibnet.ac.in/', 'is_external': True},
            {'title': 'e-Education @ CEC', 'url': 'https://cec.nic.in/', 'is_external': True}]},

 {'title': 'Our Links',
  'links': [{'title': 'Digilocker', 'url': 'https://www.digilocker.gov.in/', 'is_external': True},
            {'title': 'NSS', 'url': 'https://nss.gov.in/', 'is_external': True},
            {'title': 'NCC', 'url': 'https://indiancc.nic.in/', 'is_external': True},
            {'title': 'IQAC', 'url': '/page/iqac/', 'is_external': False},
            {'title': 'BLOG', 'url': '/page/blogs/', 'is_external': False},
           {'title': 'SWAYAM', 'url': 'https://swayam.gov.in/', 'is_external': True},
            ]},

 {'title': 'Quick Links',
  'links': [
            {'title': 'Student Services', 'url': '/page/student-services/', 'is_external': False},
            {'title': 'Placements', 'url': '/page/placements/', 'is_external': False},
            {'title': 'Research & Innovation', 'url': '/page/research-innovation/', 'is_external': False},
            {'title': 'Blogs', 'url': '/page/blogs/', 'is_external': False},
            {'title': 'Library', 'url': 'https://svu.knimbus.com/portal/v2/default/home', 'is_external': True},
            {'title': 'Contact Us', 'url': '/contact/', 'is_external': False},
            ]},
]

# --------------------------------------------------------------------------
# Homepage carousel
HERO_VIDEO = {
    # The campus banner clip, played muted on a loop.  A local file always wins
    # over the YouTube fallback below: it autoplays silently and makes no
    # third-party request.  Path is relative to ``static/``.
    'file': 'img/swamibannervideonew.mp4',

    # Only used when 'file' above is blank.
    'youtube_id': '',

    # Shown before the video paints, and to anyone on a data saver.
#     'poster': 'img/slides/slide-1.jpg',

    'headline': 'Reinvent yourself at Swami Vivekananda University',
    'subtext': 'UG, PG and Ph.D programmes across engineering, management, sciences, '
               'health, humanities, pharmacy and law. Admissions open 2026-27.',
    'cta_label': 'Apply Now',
    'cta_url': '/admission/apply/',
}

# Muted + looping is what lets a browser autoplay it at all.
HERO_VIDEO['embed_url'] = (
    'https://www.youtube-nocookie.com/embed/{id}'
    '?autoplay=1&mute=1&loop=1&playlist={id}&controls=0&showinfo=0&rel=0'
    '&modestbranding=1&iv_load_policy=3&disablekb=1&fs=0&playsinline=1'
).format(id=HERO_VIDEO['youtube_id']) if HERO_VIDEO['youtube_id'] else ''

# --------------------------------------------------------------------------
# Arrow links beside the welcome text
QUICK_LINKS = [{'title': 'Notice', 'description': 'Click to check all Notice', 'url': '/notices/'},
 {'title': 'Apply Online',
  'description': 'Join SVU by applying online and pursue your desired course.',
  'url': '/admission/apply/'},
 # Hidden for now — uncomment the block to put the card back on the homepage.
 # {'title': 'University Scholarship Foundation',
 #  'description': 'The University Scholarship Foundation offers scholarships to meritorious '
 #                 'students under special categories.',
 #  'url': '/page/scholarships/'},
 {'title': 'Schools & Courses',
  'description': "SVU schools offer multiple courses to identify and support pupil's diverse "
                 'learning needs.',
  'url': '/academics/courses/'},
 {'title': 'Industry Partners',
  'description': 'An interesting challenge in developing skills for youth and creating a '
                 'strong pipeline of talent is a seemingly…',
  'url': '/academics/industry-partners/'},
 # Hidden for now — uncomment the block to put the card back on the homepage.
#  {'title': 'SVU Facilities',
#   'description': 'The Swami Vivekananda University has one of the best-in-class infrastructure '
#                  'and facilities on the campus.',
#   'url': '/academics/facilities/'},
 ]

# --------------------------------------------------------------------------
# "Explore our offerings" band
OFFERINGS = [
#     {'title': 'Curriculum',
#   'description': 'SVU is committed to provide an effective and dynamic curriculum with a '
#                  'distinctive mission to transform lives through education.',
#   'icon': 'curriculum'},
#  {'title': 'Tech Classroom',
#   'description': 'The digital whiteboards make learning methods to be the most interactive. '
#                  'Our faculty provides academic training through smart classrooms.',
#   'icon': 'classroom'},
#  {'title': 'Experts',
#   'description': "SVU's course features expert faculty to impart quality training to the "
#                  'students.',
#   'icon': 'experts'},
#  {'title': 'Digital Library',
#   'description': 'We are pleased to offer an online storehouse of knowledge to maintain '
#                  'text-books, notes, journals, e-thesis, maps, rare books, and other important '
#                  'documents with the advent of digital technology!',
#   'icon': 'library'}
  ]

# --------------------------------------------------------------------------
# "We are now enlisted" logos
# Hidden for now — the whole band disappears from the homepage while this list
# is empty.  Uncomment the entries to bring it back; nothing else to change.
ENLISTMENTS = [
 {'title': 'Honouring Excellence, Empowering Education, Inspiring Tomorrow',
  'logo': 'img/achivements/481233106_972665624970210_8860091325710493319_n.jpg.jpeg',
  'alt_text': 'All India Management Association logo',
  'url': ''},
 
 {'title': 'A Journey of Excellence, Recognition, and Achievement',
  'logo': 'img/achivements/481979442_972665414970231_8854528053355663625_n.jpg.jpeg',
  'alt_text': 'UCEED 2026 logo',
  'url': ''},
 {'title': 'Celebrating Achievements That Inspire a Brighter Future',
  'logo': 'img/achivements/482247234_972659861637453_1522331182250338419_n.jpg.jpeg',
  'alt_text': 'Consortium of National Law Universities logo',
  'url': ''},
 {'title': 'Excellence Recognised, Achievements Celebrated, Futures Inspired',
  'logo': 'img/achivements/536270821_1105990098304428_367322835841659546_n.jpg.jpeg',
  'alt_text': 'Consortium of National Law Universities logo',
  'url': ''},
 {'title': 'Proud Moments of Academic Excellence and Achievement',
  'logo': 'img/achivements/540903586_1105990141637757_7221139477378257898_n.jpg.jpeg',
  'alt_text': 'Consortium of National Law Universities logo',
  'url': ''},
 {'title': 'From Excellence to Recognition — A Journey Worth Celebrating',
  'logo': 'img/achivements/MPTEL_2.jpeg',
  'alt_text': 'Consortium of National Law Universities logo',
  'url': ''},
 {'title': 'Where Dedication Meets Excellence and Achievement',
  'logo': 'img/achivements/MPTEL_3.jpeg',
  'alt_text': 'Consortium of National Law Universities logo',
  'url': ''},
 {'title': 'Celebrating Minds, Honouring Achievements, Inspiring Generations',
  'logo': 'img/achivements/MPTEL_4.jpeg',
  'alt_text': 'Consortium of National Law Universities logo',
  'url': ''},
 {'title': 'Recognising Excellence, Celebrating Impact',
  'logo': 'img/achivements/NPTEL_1.jpeg',
  'alt_text': 'Consortium of National Law Universities logo',
  'url': ''},

  {'title': 'Celebrating Excellence, Inspiring Achievement, Shaping the Future',
    'logo': 'img/achivements/rbangla.jpeg',
    'alt_text': 'All India Management Association logo',
    'url': ''},
 ]

# --------------------------------------------------------------------------
# The homepage slides through these two at a time.  Clicking a card opens the
# video on YouTube in a new tab — nothing plays inside the page.
#
#   title       shown in near-black
#   highlight   shown in gold, after the title (optional)
#   youtube_id  the part after "v=" in the watch URL
#   image       the picture on the card, e.g. 'img/videos/convocation.jpg'.
#               Leave it blank and YouTube's own thumbnail for that id is used,
#               so a new row works before its artwork exists.
#   url         only if the video is not on YouTube; otherwise it is built
#               from youtube_id below.
VIDEOS = [
 {'title': 'Virtual Lab',
  'highlight': 'This Lab Exists Only on Your Screen',
  'youtube_id': 'QI4D_vYJdRg',
  'image': ''},
 {'title': ' Law Moot Court',
  'highlight': 'Not a Real Court⚖️... But It Feels Exactly Like One!',
  'youtube_id': 'mWRA03EiuGo',
  'image': ''},

 # TODO: these four carry the two sample ids above so the slider has something
 # to show — swap in the real uploads and the titles are already in place.
 {'title': 'Nasha Mukt Yuva for Viksit Bharat',
  'highlight': 'A Day on Campus',
  'youtube_id': '-Vk2kn4AYVQ',
  'image': ''},
 {'title': 'OT Zones',
  'highlight': 'What Are the Different Zones in an Operation Theatre',
  'youtube_id': 'GzY85e3B8l0',
  'image': ''},
#  {'title': 'Research & Innovation',
#   'highlight': 'Inside Our Laboratories',
#   'youtube_id': 'aqz-KE-bpKQ',
#   'image': ''},
#  {'title': 'Convocation',
#   'highlight': 'Moments from the Ceremony',
#   'youtube_id': 'ScMzIvxBSi4',
#   'image': ''},
]

# 'url' is where the card sends the visitor: the ordinary YouTube watch page,
# opened in a new tab.  'thumbnail_url' is the fallback picture, used only when
# a row has no 'image' of its own.
for _video in VIDEOS:
    _video.setdefault(
        'url', 'https://www.youtube.com/watch?v=%s' % _video['youtube_id'])
    _video.setdefault(
        'thumbnail_url',
        'https://i.ytimg.com/vi/%s/hqdefault.jpg' % _video['youtube_id'])

# --------------------------------------------------------------------------
CHANCELLOR = {'name': 'The Chancellor',
 'designation': 'CHANCELLOR',
 'institution': 'SWAMI VIVEKANANDA UNIVERSITY (SVU)',
 'excerpt': 'Swami Vivekananda University continues to grow from strength to strength, '
            'consistently endeavouring to provide its students with unmatched opportunities to '
            'excel.',
 'full_message': '<p>I welcome everyone at Swami Vivekananda University. The essential information of this esteemed setup is available in this website. Since its inception, SVU has made rapid strides both in the area of academics and research. The emergence and reputation of SVU in various spheres of academia and industry reflects this rapid growth. The website has been carrying the chronological information. The inception years were really challenging due to pandemic, however, resilience shown by the staff and students helped the university in tiding over the difficult situation. I am hopeful that the SVU will match up to the societal expectation in a demand driven way. I wish SVU all success in future.</p>',
 'photo': 'img/our_team/17363489181. Chancellor.png',
 'background_image': ''}

# --------------------------------------------------------------------------
# NOT ON THE HOME PAGE ANY MORE. The band beside the Chancellor's message
# carries the Appreciations slider now. This list is kept because nothing
# else was decided for it - wire it into a page or delete it.
#
# The medallion beside each centre takes a photograph when one is set and falls
# back to the sprite icon named in 'icon' when it is not, so these can be filled
# in one at a time without anything breaking in between.
#
#   image  path under static/, e.g. 'img/centres/innovation.jpg'. Left blank
#          the icon is drawn instead. It is cropped to 4:3 and filled, so a
#          wide original keeps its edges and a tall one loses them.
#   alt_text  what the picture says, for anyone who cannot see it. With title
#          and description blank this is the ONLY text the centre has, so it
#          cannot be left empty - an image carrying the name of a centre is
#          content, not decoration.
#   icon   a symbol id from templates/includes/icons.html, minus the "i-".
# CENTRES = [
#     {'title': '',
#   'description': '',
#   'image': 'img/slides/coe.png',            # no photograph yet - the icon shows
#   'alt_text': 'Centre for Innovation & Entrepreneurship',
#   'icon': 'innovation',
#   'url': ''},

#  {'title': '',
#   'description': '',
#   'image': 'img/slides/coex.png',            # no photograph yet - the icon shows
#   'alt_text': 'Industry Collaboration',
#   'icon': 'industry',
#   'url': ''},


#  {'title': '',
#   'description': '',
#   'image': 'img/slides/ic.png',            # no photograph yet - the icon shows
#   'alt_text': 'Centre of Excellence',
#   'icon': 'excellence',
#   'url': ''},


#  {'title': '',
#   'description': "",     
#   'image': 'img/slides/ws.png',            # no photograph yet - the icon shows
#   'alt_text': 'Swami Vivekananda Centre for Women Studies',
#   'icon': 'women',
#   'url': ''}
#   ]

# --------------------------------------------------------------------------
TESTIMONIALS = [

{'name': 'Bikash Mondal',
  'role': 'Student - SVU',
  'department': 'B.Tech CSE',
  'quote': 'SVU gave me the skills, confidence, and opportunities to build a successful career.',
  'photo': 'img/student1_com.png',
  'detail_url': ''},



 {'name': 'Anup Majhi',
  'role': 'Student - SVU',
  'department': 'B.Tech CSE',
  'quote': 'SVU helped me turn my passion into the skills needed for a successful career.',
  'photo': 'img/student3_com.png',
  'detail_url': ''},



 {'name': 'Mounik Ghosh',
  'role': 'Student - SVU',
  'department': 'B.Tech CSE',
  'quote': 'My journey at SVU gave me the confidence and knowledge to achieve my career goals.', 
  'photo': 'img/student4.png',
  'detail_url': ''}]

# --------------------------------------------------------------------------
# Academics
PROGRAMS = [{'name': 'Under Graduate',
  'slug': 'under-graduate',
  'description': 'Bachelor degree programmes across engineering, science, management, media, '
                 'law and allied health.'},
 {'name': 'Post Graduate',
  'slug': 'post-graduate',
  'description': 'Master degree programmes designed for specialisation and research depth.'},
 {'name': 'Diploma',
  'slug': 'diploma',
  'description': 'Skill-focused diploma programmes with strong industry alignment.'},
 {'name': 'Ph.D',
  'slug': 'phd',
  'description': 'Doctoral research programmes guided by experienced supervisors.'}]

# --------------------------------------------------------------------------
SCHOOLS = [

    {'slug': 'school-of-engineering',
  'name': 'School of Engineering',
  'card_image': 'img/schools/soe.png',
  'short_description': 'B.Tech, M.Tech, Diploma and Ph.D programmes in computer science, '
                       'electronics, civil, mechanical and electrical engineering.',
  'description': 'The School of Engineering  is the largest school of the '
                 'university, offering a complete ladder of programmes from diploma through '
                 'doctoral research. Laboratories are mapped to the morden curriculum and '
                 'every branch runs a dedicated industry-interface cell.'
                 },


 {'slug': 'school-of-management',
  'name': 'School of Management',
  'card_image': 'img/schools/som.png',
  'short_description': 'BBA, B.Com, MBA and doctoral programmes with a strong practice and '
                       'internship component.',
  'description': 'The School of Management  builds analytical and leadership '
                 'capability through case-driven teaching, live consulting projects and summer '
                 'internships with partner organisations.'},



 {'slug': 'school-of-life-sciences',
  'name': 'School of Life Sciences',
  'card_image': 'img/schools/sls.png',
  'short_description': 'Programmes in biotechnology, microbiology,',
  'description': 'The School of Life Sciences combines molecular biology, '
                 'microbiology and food technology with well-equipped research laboratories '
                 'and active collaboration with hospitals and food industry partners.'},




 {'slug': 'school-of-allied-health-services',
  'name': 'School of Allied Health Services',
  'card_image': 'img/schools/sahs.png',
  'short_description': 'B.Sc Nursing, Post Basic Nursing, paramedical and allied health '
                       'programmes.',
  'description': 'The School of Allied Health Sciences trains clinical professionals '
                 'through simulation laboratories and supervised clinical postings in '
                 'associated hospitals.'},



 {'slug': 'school-of-humanities-social-science',
  'name': 'School of Humanities & Social Sciences',
  'card_image': 'img/schools/shss.png',
  'short_description': 'English, Sociology, Psychology, Journalism & Mass Communication and '
                       'Education.',
  'description': 'The School of Humanities & Social Sciences anchors the liberal arts core of '
                 'the university, with active departments of sociology, psychology and '
                 'journalism that regularly host national seminars.'},



 {'slug': 'school-of-basic-sciences',
  'name': 'School of Basic Sciences',
  'card_image': 'img/schools/sbs.png',
  'short_description': 'Physics, Chemistry, Mathematics and Computer Applications at UG, PG '
                       'and doctoral level.',
  'description': 'The School of Basic & Applied Sciences supports the foundation courses of '
                 'every engineering and life-science programme while running its own research '
                 'groups in materials, computation and applied mathematics.'},



#  {'slug': 'school-of-pharmacy',
#   'name': 'School of Pharmaceutical Sciences',
#   'card_image': 'img/schools/school-7.jpg',
#   'short_description': 'B.Pharm, D.Pharm and M.Pharm programmes with PCI-aligned laboratories.',
#   'description': 'The School of Pharmaceutical Sciences offers pharmacy education backed by '
#                  'pharmaceutics, pharmacology and pharmaceutical chemistry laboratories, along '
#                  'with a machine room and a herbal garden.'},




 {'slug': 'school-of-Legal-Studies',
  'name': 'School of Legal Studies',
  'card_image': 'img/schools/slaw.png',
  'short_description': 'Integrated BA LL.B, BBA LL.B and LL.M programmes with moot court '
                       'training.',
  'description': 'The School of Law & Legal Studies runs an active moot court society, legal '
                 'aid clinic and internship network across district and high courts.'},


 {
    'slug': 'school-of-agriculture',
    'name': 'School of Agriculture',
    'card_image': 'img/schools/sa.png',
    'short_description': 'Integrated education and practical training in modern agriculture, sustainable farming, and agricultural sciences.',
    'description': 'The School of Agriculture provides comprehensive education and practical training in agricultural sciences, focusing on modern farming techniques, sustainable agriculture, crop production, soil management, and agricultural technology. The school prepares students with the knowledge and skills required to contribute to the development of the agricultural sector and address emerging challenges in food security and sustainable development.'
},


{
    'slug': 'school-of-computer-science',
    'name': 'School of Computer Science',
    'card_image': 'img/schools/sca.png',
    'short_description': 'Innovative education and practical training in computer applications, data science, networking, cybersecurity, and emerging technologies.',
    'description': 'The School of Computer Science offers comprehensive education and practical training in computer applications, data science, advanced networking, cybersecurity, multimedia, and animation. The school focuses on developing strong technical knowledge, problem-solving abilities, programming skills, and industry-oriented expertise. With an emphasis on emerging technologies, hands-on learning, innovation, and research, the school prepares students for successful careers in the rapidly evolving field of computer science and information technology.'
},





]

# --------------------------------------------------------------------------
# The academic tree is School -> Department -> Course.  Every department names
# its parent school in ``school`` and every course in COURSES below names its
# parent department in ``department``, so the three levels always line up.
#
# EACH DEPARTMENT PAGE IS BUILT FROM THESE FIELDS
#   name               the heading, and the banner over the page
#   image              the photograph beside the intro.  Leave it '' and the
#                      page borrows the school's card image instead, so a
#                      department with no picture yet still looks finished.
#   short_description  one line; the card on /academics/departments/ and the
#                      page's meta description
#   description        the intro paragraph on the department page.  Leave it
#                      '' and short_description stands in.
#
# The courses, faculty and tab panel further down that page all come from
# COURSES, DEPARTMENT_FACULTY and DEPARTMENT_TABS - nothing there is written
# into the template.

DEPARTMENTS = [
 # --- School of Engineering ---
 {'slug': 'department-of-computer-science-engineering',
  'name': 'Department Of Computer Science & Engineering',
  'school': 'school-of-engineering',
  'image': 'img/departments/comp1.png',
  'short_description': 'Diploma, B.Tech, M.Tech and Ph.D programmes in computing, with laboratories '
                       'for AI, data science, networking and software engineering.',
  'description': 'Computer Science serves as the foundation for various technological advancements '
                 'that the world sees today. The field has grown by leaps and bounds and the future '
                 'innovations it brings along never seem to slow down. Yet another beauty of '
                 'computer science is that it finds a place in many interdisciplinary fields as '
                 'well. With these, there also comes a necessity to keep up to the global demand of '
                 'finding highly skilled engineers and scientists. Swami Vivekananda University, '
                 'one of the top-ranked universities in India, drives on the purpose of providing '
                 'quality education and improving competence among students, thereby living up to '
                 "its motto, 'Progress Through Knowledge'.",},
                 
 {'slug': 'department-of-civil-engineering',
  'name': 'Department Of Civil Engineering',
  'school': 'school-of-engineering',
  'image': '',
  'short_description': 'Structural, geotechnical, transportation and environmental engineering with '
                       'a full survey and materials testing laboratory.',
  'description': 'Civil engineering shapes the built environment - the buildings people live and '
                 'work in, the roads and bridges they travel over, and the water and waste systems '
                 'that let a settlement function. The department teaches structural, geotechnical, '
                 'transportation and environmental engineering alongside a full survey and '
                 'materials testing laboratory, so design work is checked against measurement from '
                 'the first year rather than the last.',},
 {'slug': 'department-of-electrical-engineering',
  'name': 'Department Of Electrical Engineering',
  'school': 'school-of-engineering',
  'image': '',
  'short_description': 'Circuits, electrical machines, power systems, control and instrumentation, '
                       'with laboratory work at every stage of the programme.',
  'description': 'Electrical engineering covers the generation, transmission and control of '
                 'electrical power and the machines that run on it. The department teaches '
                 'circuits, machines, power systems, control and instrumentation, and pairs each '
                 'subject with laboratory work so that theory is tested on equipment rather than '
                 'only on paper.',},
 {'slug': 'department-of-electronics-communication',
  'name': 'Department Of Electronics & Communication',
  'school': 'school-of-engineering',
  'image': '',
  'short_description': 'Analog and digital electronics, embedded systems, VLSI and communication '
                       'engineering.',
  'description': 'Electronics and communication engineering sits behind almost everything that '
                 'computes or connects - the devices themselves, the circuits inside them and the '
                 'networks between them. The department teaches analog and digital electronics, '
                 'embedded systems, VLSI design and communication engineering, with laboratories '
                 'where students build and measure the circuits they have designed.',},
 {'slug': 'department-of-mechanical-engineering',
  'name': 'Department Of Mechanical Engineering',
  'school': 'school-of-engineering',
  'image': '',
  'short_description': 'Advanced mechanical engineering education covering design, thermal, '
                       'manufacturing and industrial systems with hands-on CAD/CAM, workshop and '
                       'fluid mechanics laboratory training.',
  'description': 'Mechanical engineering is the broadest of the engineering disciplines, running '
                 'from the design of a single component to the operation of a whole plant. The '
                 'department covers design, thermal and fluid sciences, manufacturing and '
                 'industrial systems, supported by CAD/CAM, workshop and fluid mechanics '
                 'laboratories where students make and test what they have drawn.',},

 # --- School of Management ---
 {'slug': 'department-of-management-studies',
  'name': 'Department Of Management Studies',
  'school': 'school-of-management',
  'image': '',
  'short_description': 'BBA and MBA programmes covering marketing, finance, human resources and '
                       'operations, taught through cases and live projects.',
  'description': 'Management is learned by deciding, not only by reading about decisions. The '
                 'department teaches marketing, finance, human resources and operations through '
                 'case discussion, live projects and summer internships with partner organisations, '
                 'so students practise judgement on real situations before they are responsible for '
                 'the consequences.',},

 # --- School of Computer Science ---
 {'slug': 'department-of-computer-application',
  'name': 'Department Of Computer Application',
  'school': 'school-of-computer-science',
  'image': '',
  'short_description': 'BCA and MCA programmes covering programming, databases, web technology and '
                       'application development.',
  'description': 'Computer applications is the applied side of computing - building the software '
                 'that people actually use. The department teaches programming, databases, web '
                 'technology and application development at both bachelor and master level, with '
                 'laboratory time and project work running alongside every theory paper.',},
 {'slug': 'department-of-data-science',
  'name': 'Department Of Data Science',
  'school': 'school-of-computer-science',
  'image': '',
  'short_description': 'Statistics, machine learning and data engineering, taught with the '
                       'programming and visualisation skills that make an analysis usable.',
  'description': 'Data science turns recorded data into decisions, and it needs statistics, '
                 'programming and domain judgement in equal measure. The department teaches '
                 'statistical foundations, machine learning and data engineering together with the '
                 'visualisation and communication skills that decide whether an analysis is ever '
                 'acted on.',},
 {'slug': 'department-of-advanced-networking-cyber-security',
  'name': 'Department Of Advanced Networking & Cyber Security',
  'school': 'school-of-computer-science',
  'image': '',
  'short_description': 'Network architecture, security operations and digital forensics, taught on '
                       'equipment students configure themselves.',
  'description': 'Networks are the infrastructure everything else depends on, and securing them is '
                 'now a discipline of its own. The department teaches network architecture and '
                 'protocols alongside cryptography, security operations and digital forensics, on '
                 'laboratory equipment students configure, attack and defend themselves.',},
 {'slug': 'department-of-multimedia-animation',
  'name': 'Department Of Multimedia & Animation',
  'school': 'school-of-computer-science',
  'image': '',
  'short_description': 'Design, 2D and 3D animation, visual effects and post-production, taught as '
                       'studio practice.',
  'description': 'Animation and multimedia are craft disciplines: they are learned by making work '
                 'and having it critiqued. The department teaches design fundamentals, 2D and 3D '
                 'animation, visual effects and post-production as studio practice, so a graduate '
                 'leaves with a portfolio rather than only a transcript.',},

 # --- School of Humanities & Social Sciences ---
 {'slug': 'department-of-language-literature-cultural-studies',
  'name': 'Department Of Language, Literature And Cultural Studies',
  'school': 'school-of-humanities-social-science',
  'image': '',
  'short_description': 'Language, literature and cultural studies, with translation and critical '
                       'writing running through the programme.',
  'description': 'Literature is one of the longest records of how people have understood their own '
                 'societies, and reading it closely is a transferable skill. The department teaches '
                 'language, literature and cultural studies together, with translation work and '
                 'critical writing running through the programme rather than confined to one paper.',},
 {'slug': 'department-of-journalism-mass-communication',
  'name': 'Department Of Journalism & Mass Communication',
  'school': 'school-of-humanities-social-science',
  'image': '',
  'short_description': 'Print, broadcast and digital media practice, with an in-house studio and '
                       'editing suite.',
  'description': 'Journalism is a practical trade with an ethical spine, and both halves have to be '
                 'taught. The department covers print, broadcast and digital media practice in an '
                 'in-house studio and editing suite, alongside media law and ethics, so students '
                 'learn how to gather and verify a story as well as how to produce it.',},
 {'slug': 'department-of-education',
  'name': 'Department Of Education',
  'school': 'school-of-humanities-social-science',
  'image': '',
  'short_description': 'Teacher education covering pedagogy, curriculum design, educational '
                       'psychology and supervised classroom practice.',
  'description': 'Teaching is a profession that has to be practised under supervision before it is '
                 'practised alone. The department covers pedagogy, curriculum design, educational '
                 'psychology and assessment, and places every student in supervised classroom '
                 'practice so that method is tested against real pupils.',},

 # --- School of Allied Health Services ---
 {'slug': 'department-of-physiotherapy',
  'name': 'Department Of Physiotherapy',
  'school': 'school-of-allied-health-services',
  'image': '',
  'short_description': 'Musculoskeletal, neurological and sports physiotherapy, including a '
                       'compulsory rotating internship.',
  'description': 'Physiotherapy restores movement after injury, surgery or illness, and it is '
                 'learned hands-on. The department teaches musculoskeletal, neurological and sports '
                 'physiotherapy with electrotherapy and exercise laboratories, and every student '
                 'completes a compulsory rotating clinical internship before qualifying.',},
 {'slug': 'department-of-optometry',
  'name': 'Department Of Optometry',
  'school': 'school-of-allied-health-services',
  'image': '',
  'short_description': 'Clinical optometry, optics and vision science, with dispensing and contact '
                       'lens practice in a working clinic.',
  'description': 'Optometry is primary eye care: examining vision, detecting disease and correcting '
                 'what can be corrected. The department teaches optics and vision science alongside '
                 'clinical refraction, dispensing and contact lens practice, with clinic hours '
                 'built into the programme rather than added at the end.',},
 {'slug': 'department-of-food-nutrition',
  'name': 'Department Of Food & Nutrition',
  'school': 'school-of-allied-health-services',
  'image': '',
  'short_description': 'Human nutrition, dietetics and food science, with food analysis and diet '
                       'counselling practice.',
  'description': 'Nutrition connects laboratory science to daily life more directly than most '
                 'disciplines. The department teaches human nutrition, dietetics and food science '
                 'together with food analysis and quality control, and students practise diet '
                 'planning and counselling on real cases before they graduate.',},
 {'slug': 'department-of-psychology',
  'name': 'Department Of Psychology',
  'school': 'school-of-allied-health-services',
  'image': '',
  'short_description': 'Cognitive, clinical and counselling psychology supported by a psychological '
                       'testing laboratory.',
  'description': 'Psychology is the systematic study of behaviour and mental process, and its '
                 'methods matter as much as its findings. The department teaches cognitive, '
                 'clinical and counselling psychology supported by a psychological testing '
                 'laboratory, with research method and statistics taught as a working skill rather '
                 'than a hurdle.',},
 {'slug': 'department-of-medical-laboratory-technology',
  'name': 'Department Of Medical Laboratory Technology',
  'school': 'school-of-allied-health-services',
  'image': '',
  'short_description': 'Clinical biochemistry, pathology, haematology and microbiology, taught in '
                       'working diagnostic laboratories.',
  'description': 'Most clinical decisions rest on a laboratory result, which makes the accuracy of '
                 'that result a patient-safety question. The department teaches clinical '
                 'biochemistry, pathology, haematology and microbiology in working diagnostic '
                 'laboratories, with quality control and sample handling treated as core subjects.',},
 {'slug': 'department-of-medical-radiology-imaging-technology',
  'name': 'Department Of Medical Radiology & Imaging Technology',
  'school': 'school-of-allied-health-services',
  'image': '',
  'short_description': 'Radiography, imaging physics and radiation safety, with supervised practice '
                       'on diagnostic equipment.',
  'description': 'Medical imaging is how much of modern diagnosis is done, and operating it well is '
                 'a technical and a safety discipline at once. The department teaches radiographic '
                 'technique, imaging physics and radiation protection, with supervised practice on '
                 'diagnostic equipment throughout the programme.',},

 # --- School of Legal Studies ---
 {'slug': 'department-of-legal-studies',
  'name': 'Department Of Legal Studies',
  'school': 'school-of-Legal-Studies',
  'image': '',
  'short_description': 'Integrated and postgraduate law programmes with moot court training, a '
                       'legal aid clinic and court internships.',
  'description': 'Law is argued, not recited, so advocacy is taught from the beginning. The '
                 'department runs integrated and postgraduate law programmes with moot court '
                 'training, a legal aid clinic and court internships, so students appear, draft and '
                 'advise under supervision long before they are admitted to practice.',},

 # --- School of Life Sciences ---
 {'slug': 'department-of-biotechnology',
  'name': 'Department Of Biotechnology',
  'school': 'school-of-life-sciences',
  'image': '',
  'short_description': 'Molecular biology, genetic engineering and bioprocess technology at '
                       'undergraduate and postgraduate level.',
  'description': 'Biotechnology puts living systems to work, and it is a laboratory subject before '
                 'it is anything else. The department teaches molecular biology, genetic '
                 'engineering and bioprocess technology at undergraduate and postgraduate level, '
                 'with bench work and project research running through both.',},
 {'slug': 'department-of-microbiology',
  'name': 'Department Of Microbiology',
  'school': 'school-of-life-sciences',
  'image': '',
  'short_description': 'Medical, industrial and food microbiology with a dedicated culture and '
                       'fermentation laboratory.',
  'description': 'Microbiology underpins medicine, food safety and much of industry, and all three '
                 'are taught here. The department covers medical, industrial and food microbiology '
                 'with a dedicated culture and fermentation laboratory, where students handle, '
                 'identify and cultivate organisms themselves.',},

 # --- School of Basic Sciences ---
 {'slug': 'department-of-mathematics',
  'name': 'Department Of Mathematics',
  'school': 'school-of-basic-sciences',
  'image': '',
  'short_description': 'Pure and applied mathematics, numerical methods and the foundation courses '
                       'that run across every engineering programme.',
  'description': 'Mathematics is both a subject in its own right and the language the other '
                 'sciences are written in. The department teaches pure and applied mathematics, '
                 'numerical methods and statistics, and also runs the foundation courses that sit '
                 'under every engineering and science programme in the university.',},
 {'slug': 'department-of-chemistry',
  'name': 'Department Of Chemistry',
  'school': 'school-of-basic-sciences',
  'image': '',
  'short_description': 'Organic, inorganic, physical and analytical chemistry, with instrumentation '
                       'and synthesis laboratories.',
  'description': 'Chemistry explains what materials are made of and how they can be changed, which '
                 'puts it under medicine, materials and energy alike. The department teaches '
                 'organic, inorganic, physical and analytical chemistry, with synthesis and '
                 'instrumentation laboratories where students run and interpret their own analyses.',},
 {'slug': 'department-of-physics',
  'name': 'Department Of Physics',
  'school': 'school-of-basic-sciences',
  'image': '',
  'short_description': 'Classical and modern physics, electronics and computational methods, with '
                       'optics and condensed matter laboratories.',
  'description': 'Physics is the foundation the engineering disciplines are built on, and it is '
                 'taught here as an experimental subject. The department covers classical and '
                 'modern physics, electronics and computational methods, with optics, electronics '
                 'and condensed matter laboratories where students measure the effects they have '
                 'just derived.',},

 # --- School of Agriculture ---
 {'slug': 'department-of-agriculture',
  'name': 'Department Of Agriculture',
  'school': 'school-of-agriculture',
  'image': '',
  'short_description': 'Agronomy, soil science, horticulture and agricultural extension, taught on '
                       "the university's own plots.",
  'description': 'Agriculture is a field science, and it cannot be learned entirely indoors. The '
                 'department teaches agronomy, soil science, horticulture, plant protection and '
                 "agricultural extension, with practical work on the university's own plots and "
                 'attachments with farms and extension agencies in the surrounding districts.',}]




# --------------------------------------------------------------------------
# Faculty shown in the auto-sliding carousel on a department page.
#
#   KEY   = the department ``slug`` from DEPARTMENTS above.
#   VALUE = a list of teachers, in the order they should appear.
#
# A department with no key here simply shows no faculty section, so add a new
# block the moment you have the names.  Every field is optional except
# ``name``:
#   photo         'img/faculty/somebody.jpg' — omit it for the grey avatar.
#   profile_url   link for "Read More"; omit it and the link disappears.
DEPARTMENT_FACULTY = {
 'department-of-computer-science-engineering': [
  {'name': 'Prof.Somsubhra Gupta',
   'designation': 'Professor',
   'photo': '',
   'qualification': 'Ph.D.',
   'publications': '250+',
   'experience': '25+ years',
   'research_area': 'Machine Learning, Computer Vision',
   'profile_url': ''},

  {'name': 'Ranjan kumar Mondal',
   'designation': 'Assistant Professor',
   'photo': '',
   'qualification': 'M.Tech, Ph.D. (pursuing)',
   'publications': '14 papers',
   'experience': '8 years',
   'research_area': 'Cyber Security, Network Forensics',
   'profile_url': ''},
  {'name': 'Sourav Saha',
   'designation': 'Assistant Professor',
   'photo': '',
   'qualification': 'M.Tech (Computer Science & Engineering)',
   'publications': '9 papers',
   'experience': '6 years',
   'research_area': 'Data Mining, Natural Language Processing',
   'profile_url': ''},
  {'name': 'Jayanta chowdhury',
   'designation': 'Assistant Professor',
   'photo': '',
   'qualification': 'M.Tech (Computer Science & Engineering)',
   'publications': '9 papers',
   'experience': '6 years',
   'research_area': 'Data Mining, Natural Language Processing',
   'profile_url': ''},
  {'name': 'Apurba Sarkar',
   'designation': 'Assistant Professor',
   'photo': '',
   'qualification': 'M.Tech cse',
   'publications': '7 papers',
   'experience': '3 years',
   'research_area': 'Machine Learning, Automation',
   'profile_url': 'img/faculty/Apurba sarkar.pdf'},
 ],
}

# --------------------------------------------------------------------------
# The tab panel on a department page: Mission & Vision, Core Values and so on.
#
#   KEY   = the department ``slug``.  A department without its own entry falls
#           back to DEFAULT_DEPARTMENT_TABS below, where the text "{department}"
#           is replaced by the department name — so every department already
#           reads correctly before anyone writes bespoke copy for it.
#
# Each tab is a dict:
#   title    the pill label (keep it short — it has to fit the pill)
#   heading  the h3 above the content; defaults to ``title`` when omitted
#   intro    one paragraph before the list
#   icon     sprite id without the "i-" prefix (book, research, users,
#            innovation, industry, graduation, handshake, excellence, lab…)
#   points   [{'label': 'Education', 'text': '…'}] — the icon rows
#   body     ['paragraph', 'paragraph'] for a prose tab such as Message Desk
#   signature {'name': …, 'role': …} printed under a prose tab
DEPARTMENT_TABS = {
 'department-of-computer-science-engineering': [

  {'title': 'Mission & Vision',
   'icon': 'book',
   'intro': 'The primary goal of the Department of Computer Science and Engineering is to '
            'advance knowledge and education in the fields of computer science and '
            'engineering. The department serves various objectives, including:',
   'points': [
    {'label': 'Education',
     'text': 'The department aims to provide high-quality education to students at various '
             'levels, including undergraduate, graduate and doctoral programmes. The goal is '
             'to equip students with a solid foundation in computer science and engineering '
             'principles, theories and practical skills.'},
    {'label': 'Research',
     'text': 'One of the key goals is to advance the state of knowledge in computer science '
             'and engineering through research. Faculty members and students engage in '
             "cutting-edge research projects that lead to innovations, discoveries and "
             "contributions to the field's body of knowledge."},
    {'label': 'Innovation',
     'text': 'The department fosters an environment that encourages innovation and '
             'entrepreneurship, incubating new ideas, technologies and startups that address '
             'real-world problems and contribute to societal progress.'},
    {'label': 'Technology Transfer',
     'text': 'In collaboration with industry partners, the department works on technology '
             'transfer initiatives, facilitating the application of research findings in '
             'practical settings through licensing and industry-sponsored projects.'},
    {'label': 'Professional Development',
     'text': 'The department focuses on the professional development of its students by '
             'providing internships, co-op programmes and industry connections, preparing '
             'them for successful careers in computing.'},
   ]},

  {'title': 'Core Values',
   'icon': 'excellence',
   'intro': 'Everything the department does rests on a small set of commitments that shape '
            'how we teach, research and work together.',
   'points': [
    {'label': 'Integrity',
     'text': 'Honest conduct in examinations, research and publication, upheld by a clear '
             'academic-integrity policy that students learn from their first semester.'},
    {'label': 'Excellence',
     'text': 'Continuous improvement of curriculum, laboratories and teaching practice, '
             'measured through structured feedback every semester.'},
    {'label': 'Collaboration',
     'text': 'Open exchange between students, faculty, industry partners and other '
             'institutions, because the best work here is rarely done alone.'},
    {'label': 'Inclusivity',
     'text': 'An environment where every student is supported regardless of background, '
             'with mentoring and remedial classes for those who need them.'},
    {'label': 'Lifelong Learning',
     'text': 'Graduates who can teach themselves the next technology, which matters more in '
             'computing than any single tool taught in class.'},
   ]},

  {'title': 'Salient Features',
   'icon': 'lab',
   'intro': 'What a student actually gets access to in this department:',
   'points': [
    {'label': 'Modern Laboratories',
     'text': 'Dedicated laboratories for programming, networking, data science, cyber '
             'security and project work, open beyond class hours.'},
    {'label': 'Industry-Aligned Curriculum',
     'text': 'Syllabus reviewed with industry members on the Board of Studies, with electives '
             'that track current practice rather than lagging behind it.'},
    {'label': 'Experienced Faculty',
     'text': 'Doctorate and postgraduate faculty with research publications and industry '
             'experience, at a healthy student-to-teacher ratio.'},
    {'label': 'Research Culture',
     'text': 'Undergraduate students are attached to research groups and encouraged to '
             'publish, present at conferences and file patents.'},
    {'label': 'Training & Placement',
     'text': 'Aptitude, coding and interview training from the pre-final year, run by the '
             'central training and placement cell.'},
   ]},

  {'title': 'Why This Department',
   'icon': 'graduation',
   'intro': 'Reasons students give for choosing computer science and engineering here:',
   'points': [
    {'label': 'A Complete Ladder',
     'text': 'Diploma, B.Tech, M.Tech and Ph.D under one roof, so a student can continue '
             'without changing institutions.'},
    {'label': 'Hands-On From Year One',
     'text': 'Laboratory and project work begins in the first year instead of waiting for '
             'the final-year project.'},
    {'label': 'Certifications',
     'text': 'Value-added certification courses run alongside the degree, in cloud, data and '
             'security tracks.'},
    {'label': 'Startup Support',
     'text': 'Student projects with commercial potential are routed to the Centre for '
             'Innovation & Entrepreneurship for incubation.'},
   ]},

  {'title': 'Message Desk',
   'icon': 'users',
   # Sits to the left of the message. Swap in the head of department's
   # photograph; drop the key and the text simply runs full width.
   'image': 'img/about/campus.jpg',
   'body': [
    'Welcome to the Department of Computer Science and Engineering. Computing changes faster '
    'than any syllabus can be revised, so our work here is less about teaching you a fixed '
    'set of tools and more about building the foundation that lets you pick up the next one '
    'on your own.',
    'Our faculty combine teaching with active research, and our laboratories stay open for '
    'students who want to build something beyond the prescribed practicals. If you are '
    'considering this department, come and see the campus — talk to the students, not just '
    'the prospectus.',
   ],
   'signature': {'name': 'Head of the Department',
                 'role': 'Department of Computer Science & Engineering'}},
 ],
}

# Used for any department that has no entry in DEPARTMENT_TABS above.
# "{department}" is swapped for the SUBJECT when the page renders - the
# department name with its "Department Of" prefix taken off, so that
# "the Department of {department}" reads "the Department of Physics"
# rather than doubling the words.
DEFAULT_DEPARTMENT_TABS = [

 {'title': 'Mission & Vision',
  'icon': 'book',
  'intro': 'The primary goal of the Department of {department} is to advance knowledge and '
           'education in its field. The department serves various objectives, including:',
  'points': [
   {'label': 'Education',
    'text': 'Providing high-quality education at undergraduate, postgraduate and doctoral '
            'level, equipping students with a solid foundation in both principles and '
            'practical skills.'},
   {'label': 'Research',
    'text': 'Advancing the state of knowledge through research, with faculty and students '
            'working on projects that contribute to the discipline.'},
   {'label': 'Innovation',
    'text': 'Encouraging innovation and entrepreneurship, and supporting ideas that address '
            'real-world problems.'},
   {'label': 'Professional Development',
    'text': 'Preparing students for their careers through internships, industry connections '
            'and structured training.'},
  ]},

 {'title': 'Core Values',
  'icon': 'excellence',
  'intro': 'The commitments that shape how the Department of {department} teaches and works.',
  'points': [
   {'label': 'Integrity',
    'text': 'Honest conduct in study, assessment and research, upheld by a clear academic '
            'integrity policy.'},
   {'label': 'Excellence',
    'text': 'Continuous improvement of curriculum, laboratories and teaching, guided by '
            'student feedback each semester.'},
   {'label': 'Collaboration',
    'text': 'Open exchange between students, faculty, industry partners and other '
            'institutions.'},
   {'label': 'Inclusivity',
    'text': 'Support for every student regardless of background, with mentoring for those '
            'who need it.'},
  ]},

 {'title': 'Salient Features',
  'icon': 'lab',
  'intro': 'What a student gets access to in the Department of {department}:',
  'points': [
   {'label': 'Well-Equipped Laboratories',
    'text': 'Practical work is mapped to the syllabus, with laboratories open beyond '
            'scheduled class hours.'},
   {'label': 'Industry-Aligned Curriculum',
    'text': 'The syllabus is reviewed with industry members on the Board of Studies.'},
   {'label': 'Experienced Faculty',
    'text': 'Doctorate and postgraduate faculty at a healthy student-to-teacher ratio.'},
   {'label': 'Training & Placement',
    'text': 'Aptitude and interview training from the pre-final year, run by the central '
            'training and placement cell.'},
  ]},

 {'title': 'Why This Department',
  'icon': 'graduation',
  'intro': 'Reasons students give for choosing the Department of {department} here:',
  'points': [
   {'label': 'Hands-On From Year One',
    'text': 'Laboratory and field work begins early rather than waiting for the final-year '
            'project.'},
   {'label': 'Mentoring',
    'text': 'Every student is attached to a faculty mentor who follows their progress across '
            'the programme.'},
   {'label': 'Certifications',
    'text': 'Value-added certification courses run alongside the degree.'},
  ]},

 # Every department page carries this fifth tab, so they all read the same
 # way. "{department}" is swapped for the subject - see the note above -
 # and that applies inside the signature too. Give a department its own
 # block in DEPARTMENT_TABS above to replace this with a message actually
 # written by its head.
 {'title': 'Message Desk',
  'icon': 'users',
  'image': 'img/about/campus.jpg',
  'body': [
   'Welcome to the Department of {department}. Our work here is less about '
   'teaching a fixed set of tools than about building the foundation that lets '
   'a graduate pick up the next one on their own, because every discipline '
   'changes faster than a syllabus can be revised.',
   'Our faculty combine teaching with active research, and our laboratories '
   'stay open to students who want to build something beyond the prescribed '
   'practicals. Alongside the syllabus we run projects, industry visits and '
   'certification courses, so a student leaves with a record of work as well '
   'as a transcript.',
   'If you are considering this department, come and see the campus - talk to '
   'the students and the teachers, not just the prospectus.',
  ],
  'signature': {'name': 'Head of the Department',
                'role': 'Department of {department}'}},
]

# --------------------------------------------------------------------------
# Banner behind the course title, one per SCHOOL — every course in that school
# picks it up. Empty, so all of them currently show the campus banner.
#
# Fill a line in to give a whole school its own, e.g.
#     'school-of-engineering': 'img/banners/engineering.jpg',
# and drop the file in static/img/banners/. The key is the school slug, the
# same one the course rows use.
#
# WHAT MAKES A GOOD ONE: wide and short — around 1440x300 — with nothing
# important across the middle, because that is where the title sits. It is
# laid at about a third opacity over the dark ground, so a busy photograph is
# fine, but a picture with WORDING PAINTED INTO IT is not: cropped to this
# shape the words get cut in half and read as a mistake behind the title.
# That is why the school pictures used elsewhere on the site are not used
# here — they have the school name across them.
#
# A single course can override its school with 'hero_image' on its own row.
COURSE_BANNERS = {}

# --------------------------------------------------------------------------
# Courses  —  /academics/courses/[slug]/
#
# THE TWO PICTURES ON A COURSE PAGE, and they are not the same one:
#
#   hero_image   the wide banner BEHIND the course title at the top. Optional,
#                and only needed to override the school-wide one: left blank,
#                the course takes its school's entry in COURSE_BANNERS above,
#                and failing that the campus banner. So every course has one
#                without a word being typed here.
#
#                See COURSE_BANNERS for what makes a good picture — the short
#                version is wide, short, and nothing important in the middle.
#
#   card_image   the picture in the intro band lower down, and on the course
#                card in listings. Its own ladder, finest first: the course's
#                own picture, then its department's, then its school's.
#
# Both take a path under static/, e.g. 'img/courses/civil-banner.jpg'. Drop
# the file in, name it here, run
#     python manage.py collectstatic --noinput
# and it appears. A name that does not match a file costs that one picture
# rather than the page — the banner just goes back to its plain dark ground.
COURSES = [

#civil start
 {
    'slug': 'diploma-in-civil-engineering',
    'name': 'Diploma in Civil Engineering',
    'badge': 'Diploma',
    'card_image': '',
    'careers': [
        'Software Engineer',
        'Hardware Engineer',
        'Networking Engineer',
        'Software Tester',
        'Web Designer',
        'App Developer',
        'Project Engineer',
        'IT Engineer',
        'Technical Support Engineer',
        'Voice Process Support Engineer',
    ],
    'school': 'school-of-engineering',
    'department': 'department-of-civil-engineering',
    'program': 'under-graduate',
    'duration': '3 Years',
    'total_seats': 120,
    'is_featured': True,
    'eligibility': 'Passed 10th standard or equivalent examination from a recognised board with a minimum of 50% marks.',
    'description': 'The programme blends classroom instruction, laboratory or field practice and continuous internal assessment. Students are mentored throughout the course and prepared for placement through the training and placement cell.'
},

{
    'slug': 'b-tech-in-civil-engineering',
    'name': 'B.Tech in Civil Engineering',
    'badge': 'B.Tech',
    'card_image': '',
    'careers': [
        'Software Engineer',
        'Systems Analyst',
        'Full Stack Developer',
        'Data Engineer',
        'Cloud Engineer',
        'Cybersecurity Analyst',
    ],
    'school': 'school-of-engineering',
    'department': 'department-of-civil-engineering',
    'program': 'under-graduate',
    'duration': '4 Years',
    'total_seats': 120,
    'is_featured': True,
    'eligibility': 'Passed 10+2 with Physics, Chemistry and Mathematics as main subjects and a minimum of 50% aggregate from a recognised board.',
    'description': 'The programme blends classroom instruction, laboratory or field practice and continuous internal assessment. Students are mentored throughout the course and prepared for placement through the training and placement cell.'
},


{
    'slug': 'm-tech-in-civil-engineering',
    'name': 'M.Tech in Civil Engineering',
    'badge': 'M.Tech',
    'card_image': '',
    'careers': [
        'Senior Software Engineer',
        'Machine Learning Engineer',
        'Solution Architect',
        'Research Engineer',
        'Academic Faculty',
    ],
    'school': 'school-of-engineering',
    'department': 'department-of-civil-engineering',
    'program': 'post-graduate',
    'duration': '2 Years',
    'total_seats': 60,
    'is_featured': True,
    'eligibility': 'Passed B.Tech or B.E. in Civil Engineering from a recognised university with a minimum of 50% aggregate marks.',
    'description': 'The programme provides advanced knowledge in civil engineering through specialised coursework, practical laboratory training, research-oriented learning and project work. Students are mentored throughout the course and prepared for advanced technical careers, research and higher studies.'
},

{
    'slug': 'phd-in-civil-engineering',
    'name': 'Ph.D. in Civil Engineering',
    'badge': 'Ph.D.',
    'card_image': '',
    'careers': [
        'Research Scientist',
        'Assistant Professor',
        'Principal Investigator',
        'Research and Development Lead',
    ],
    'school': 'school-of-engineering',
    'department': 'department-of-civil-engineering',
    'program': 'phd',
    'duration': '5 Years',
    'total_seats': 20,
    'is_featured': True,
    'eligibility': 'Master’s degree in Civil Engineering from a recognised university with a minimum of 55% aggregate marks. Candidates may be required to qualify through the university admission process, including an entrance examination and/or interview.',
    'description': 'The Ph.D. programme in Civil Engineering focuses on advanced research, innovation and specialised study in emerging areas of civil engineering. Scholars undertake research under expert faculty guidance, complete required coursework and develop an original research thesis contributing to the field.'
},

#civil end

#cse start
 {
    'slug': 'diploma-in-computer-science-technology',
    'name': 'Diploma in Computer Science & Technology',
    'badge': 'Diploma',
    'card_image': '',
    'careers': [
        'Software Engineer',
        'Hardware Engineer',
        'Networking Engineer',
        'Software Tester',
        'Web Designer',
        'App Developer',
        'Project Engineer',
        'IT Engineer',
        'Technical Support Engineer',
        'Voice Process Support Engineer',
    ],
    'school': 'school-of-engineering',
    'department': 'department-of-computer-science-engineering',
    'program': 'under-graduate',
    'duration': '3 Years',
    'total_seats': 120,
    'is_featured': True,
    'eligibility': 'Passed 10th standard or equivalent examination from a recognised board with a minimum of 50% marks.',
    'description': 'The programme blends classroom instruction, laboratory or field practice and continuous internal assessment. Students are mentored throughout the course and prepared for placement through the training and placement cell.'
},

{
    'slug': 'b-tech-in-computer-science-engineering',
    'name': 'B.Tech in Computer Science & Engineering',
    'badge': 'B.Tech',
    'card_image': '',
    'careers': [
        'Software Engineer',
        'Systems Analyst',
        'Full Stack Developer',
        'Data Engineer',
        'Cloud Engineer',
        'Cybersecurity Analyst',
    ],
    'school': 'school-of-engineering',
    'department': 'department-of-computer-science-engineering',
    'program': 'under-graduate',
    'duration': '4 Years',
    'total_seats': 120,
    'is_featured': True,
    'eligibility': 'Passed 10+2 with Physics, Chemistry and Mathematics as main subjects and a minimum of 50% aggregate from a recognised board.',
    'description': 'The programme blends classroom instruction, laboratory or field practice and continuous internal assessment. Students are mentored throughout the course and prepared for placement through the training and placement cell.'
},


{
    'slug': 'm-tech-in-computer-science-engineering',
    'name': 'M.Tech in Computer Science & Engineering',
    'badge': 'M.Tech',
    'card_image': '',
    'careers': [
        'Senior Software Engineer',
        'Machine Learning Engineer',
        'Solution Architect',
        'Research Engineer',
        'Academic Faculty',
    ],
    'school': 'school-of-engineering',
    'department': 'department-of-computer-science-engineering',
    'program': 'post-graduate',
    'duration': '2 Years',
    'total_seats': 60,
    'is_featured': True,
    'eligibility': 'Passed B.Tech or B.E. in Computer Science & Engineering, Information Technology, or a related engineering discipline from a recognised university with a minimum of 50% aggregate marks.',
    'description': 'The programme provides advanced knowledge in computer science and engineering through specialised coursework, practical laboratory training, research-oriented learning and project work. Students are mentored throughout the course and prepared for advanced technical careers, research and higher studies.'
},

{
    'slug': 'phd-in-computer-science-engineering',
    'name': 'Ph.D. in Computer Science & Engineering',
    'badge': 'Ph.D.',
    'card_image': '',
    'careers': [
        'Research Scientist',
        'Assistant Professor',
        'Principal Investigator',
        'Research and Development Lead',
    ],
    'school': 'school-of-engineering',
    'department': 'department-of-computer-science-engineering',
    'program': 'phd',
    'duration': '5 Years',
    'total_seats': 20,
    'is_featured': True,
    'eligibility': 'Master’s degree in Computer Science & Engineering, Information Technology, Computer Applications, or a related discipline from a recognised university with a minimum of 55% aggregate marks. Candidates may be required to qualify through the university admission process, including an entrance examination and/or interview.',
    'description': 'The Ph.D. programme in Computer Science & Engineering focuses on advanced research, innovation and specialised study in emerging areas of computing. Scholars undertake research under expert faculty guidance, complete required coursework and develop an original research thesis contributing to the field.'
},

#cse end

#ee start
 {
    'slug': 'diploma-in-electrical-engineering',
    'name': 'Diploma in Electrical Engineering',
    'badge': 'Diploma',
    'card_image': '',
    'careers': [
        'Software Engineer',
        'Hardware Engineer',
        'Networking Engineer',
        'Software Tester',
        'Web Designer',
        'App Developer',
        'Project Engineer',
        'IT Engineer',
        'Technical Support Engineer',
        'Voice Process Support Engineer',
    ],
    'school': 'school-of-engineering',
    'department': 'department-of-electrical-engineering',
    'program': 'under-graduate',
    'duration': '3 Years',
    'total_seats': 120,
    'is_featured': True,
    'eligibility': 'Passed 10th standard or equivalent examination from a recognised board with a minimum of 50% marks.',
    'description': 'The programme blends classroom instruction, laboratory or field practice and continuous internal assessment. Students are mentored throughout the course and prepared for placement through the training and placement cell.'
},

{
    'slug': 'b-tech-in-electrical-engineering',
    'name': 'B.Tech in Electrical Engineering',
    'badge': 'B.Tech',
    'card_image': '',
    'careers': [
        'Software Engineer',
        'Systems Analyst',
        'Full Stack Developer',
        'Data Engineer',
        'Cloud Engineer',
        'Cybersecurity Analyst',
    ],
    'school': 'school-of-engineering',
    'department': 'department-of-electrical-engineering',
    'program': 'under-graduate',
    'duration': '4 Years',
    'total_seats': 120,
    'is_featured': True,
    'eligibility': 'Passed 10+2 with Physics, Chemistry and Mathematics as main subjects and a minimum of 50% aggregate from a recognised board.',
    'description': 'The programme blends classroom instruction, laboratory or field practice and continuous internal assessment. Students are mentored throughout the course and prepared for placement through the training and placement cell.'
},


{
    'slug': 'm-tech-in-electrical-engineering',
    'name': 'M.Tech in Electrical Engineering',
    'badge': 'M.Tech',
    'card_image': '',
    'careers': [
        'Senior Software Engineer',
        'Machine Learning Engineer',
        'Solution Architect',
        'Research Engineer',
        'Academic Faculty',
    ],
    'school': 'school-of-engineering',
    'department': 'department-of-electrical-engineering',
    'program': 'post-graduate',
    'duration': '2 Years',
    'total_seats': 60,
    'is_featured': True,
    'eligibility': 'Passed B.Tech or B.E. in Electrical Engineering from a recognised university with a minimum of 50% aggregate marks.',
    'description': 'The programme provides advanced knowledge in electrical engineering through specialised coursework, practical laboratory training, research-oriented learning and project work. Students are mentored throughout the course and prepared for advanced technical careers, research and higher studies.'
},
# ee end



# ece start
 {'slug': 'b-tech-in-electronics-communication-engineering',
  'name': 'B.Tech in Electronics & Communication Engineering',
  'badge': 'B.Tech',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-engineering',
  'department': 'department-of-electronics-communication',
  'program': 'under-graduate',
  'duration': '4 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed 10+2 with Physics, Chemistry and Mathematics as main subjects and a '
                 'minimum of 50% aggregate from a recognised board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


 {'slug': 'm-tech-in-electronics-communication-engineering',
  'name': 'M.Tech in Electronics & Communication Engineering',
  'badge': 'M.Tech',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-engineering',
  'department': 'department-of-electronics-communication',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed B.Tech or B.E. in Electronics & Communication Engineering from a recognised university with a minimum of 50% aggregate marks.',
  'description': 'The programme provides advanced knowledge in electronics and communication engineering through specialised coursework, practical laboratory training, research-oriented learning and project work. Students are mentored throughout the course and prepared for advanced technical careers, research and higher studies.'},

# ece end


#me start
{'slug': 'diploma-in-mechanical-engineering',
  'name': 'Diploma in Mechanical Engineering',
  'badge': 'Diploma',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-engineering',
  'department': 'department-of-mechanical-engineering',
  'program': 'under-graduate',
  'duration': '4 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 with Physics, Chemistry and Mathematics as main subjects and a '
                 'minimum of 50% aggregate from a recognised board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},



 {'slug': 'b-tech-in-mechanical-engineering',
  'name': 'B.Tech in Mechanical Engineering',
  'badge': 'B.Tech',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-engineering',
  'department': 'department-of-mechanical-engineering',
  'program': 'under-graduate',
  'duration': '4 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 with Physics, Chemistry and Mathematics as main subjects and a '
                 'minimum of 50% aggregate from a recognised board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

 {'slug': 'm-tech-in-mechanical-engineering',
  'name': 'M.Tech in Mechanical Engineering',
  'badge': 'M.Tech',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-engineering',
  'department': 'department-of-mechanical-engineering',
  'program': 'under-graduate',
  'duration': '4 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 with Physics, Chemistry and Mathematics as main subjects and a '
                 'minimum of 50% aggregate from a recognised board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

 {'slug': 'phd-in-mechanical-engineering',
  'name': 'PhD in Mechanical Engineering',
  'badge': 'PhD',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-engineering',
  'department': 'department-of-mechanical-engineering',
  'program': 'under-graduate',
  'duration': '4 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 with Physics, Chemistry and Mathematics as main subjects and a '
                 'minimum of 50% aggregate from a recognised board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},



  #me end 
 
#  management start
 {'slug': 'bachelor-of-business-administration-bba',
  'name': 'Bachelor of Business Administration (BBA)',
  'badge': 'BBA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-management',
  'department': 'department-of-management-studies',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': True,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


 {'slug': 'bachelor-of-business-administration-digital-marketing',
  'name': 'Bachelor of Business Administration (Digital Marketing)',
  'badge': 'BBA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-management',
  'department': 'department-of-management-studies',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


 {'slug': 'bachelor-of-business-administration-hospital-management',
  'name': 'Bachelor of Business Administration (Hodpital Management)',
  'badge': 'MBA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-management',
  'department': 'department-of-management-studies',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': "Bachelor's degree in any discipline with a minimum of 50% aggregate. Valid "
                 'MAT / CAT / CMAT score is preferred.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},



 {'slug': 'bachelor-of-business-administration-hotel-hospital-management',
  'name': 'Bachelor of Business Administration (Hotel Hodpital Management)',
  'badge': 'MBA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-management',
  'department': 'department-of-management-studies',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': "Bachelor's degree in any discipline with a minimum of 50% aggregate. Valid "
                 'MAT / CAT / CMAT score is preferred.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

 {'slug': 'master-of-business-administration',
  'name': 'Master of Business Administration',
  'badge': 'MBA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-management',
  'department': 'department-of-management-studies',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': "Bachelor's degree in any discipline with a minimum of 50% aggregate. Valid "
                 'MAT / CAT / CMAT score is preferred.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

#  management end


#biotechnology start

 {'slug': 'b-sc-in-biotechnology',
  'name': 'Bachelor of Science (Hons.) in Biotechnology',
  'badge': 'B.Sc',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-life-sciences',
  'department': 'department-of-biotechnology',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed 10+2 in the science stream with Biology / Biotechnology and a minimum '
                 'of 45% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


 {'slug': 'm-sc-in-biotechnology',
  'name': 'Master of Science in Biotechnology',
  'badge': 'M.Sc',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-life-sciences',
  'department': 'department-of-biotechnology',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed 10+2 in the science stream with Biology / Biotechnology and a minimum '
                 'of 45% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

#biotechnology end

#microbiology start
 {'slug': 'b-sc-in-microbiology',
  'name': 'Bachelor of Science (Hons.) in Microbiology',
  'badge': 'B.Sc',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-life-sciences',
  'department': 'department-of-microbiology',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in the science stream with Biology and a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


 {'slug': 'm-sc-in-microbiology',
  'name': 'Master of Science in Microbiology',
  'badge': 'M.Sc',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-life-sciences',
  'department': 'department-of-microbiology',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 30,
  'is_featured': False,
  'eligibility': 'B.Sc in Biotechnology, Microbiology, Zoology, Botany or an allied '
                 'life-science discipline with a minimum of 50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 
 #microbiology end


 #Physiotherapy start 

 {'slug': 'bachelor-of-physiotherapy',
  'name': 'Bachelor of Physiotherapy',
  'badge': 'BPT',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-allied-health-services',
  'department': 'department-of-physiotherapy',
  'program': 'under-graduate',
  'duration': '4.5 Years',
  'total_seats': 40,
  'is_featured': False,
  'eligibility': 'Passed 10+2 with Physics, Chemistry and Biology, securing a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

 {'slug': 'master-of-physiotherapy',
  'name': 'Master of Physiotherapy',
  'badge': 'MPT',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-allied-health-services',
  'department': 'department-of-physiotherapy',
  'program': 'post-graduate',
  'duration': '4.5 Years',
  'total_seats': 40,
  'is_featured': False,
  'eligibility': 'Passed 10+2 with Physics, Chemistry and Biology, securing a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

# Physiotherapy end

#jmc start

 {'slug': 'ba-honours-in-journalism-mass-communication',
  'name': 'BA (Honours) in Journalism & Mass Communication',
  'badge': 'BA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-humanities-social-science',
  'department': 'department-of-journalism-mass-communication',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

 {'slug': 'ma-honours-in-journalism-mass-communication',
  'name': 'M.A in Journalism & Mass Communication',
  'badge': 'MA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-humanities-social-science',
  'department': 'department-of-journalism-mass-communication',
  'program': 'post-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

     #jmc end


#psychology start
                 
 {'slug': 'master-applied-psychology',
  'name': 'M.Sc. / M.A in Applied Psychology (Specialization in Clinical Psychology)',
  'badge': 'MA/MSc',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-allied-health-services',
  'department': 'department-of-psychology',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


 #psychology end





#computer application start
 {'slug': 'bachelor-of-computer-applications',
  'name': 'Bachelor of Computer Applications',
  'badge': 'BCA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-computer-science',
  'department': 'department-of-computer-application',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': True,
  'eligibility': 'Passed 10+2 with Mathematics or Computer Science and a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},



 {'slug': 'master-of-computer-applications',
  'name': 'Master of Computer Applications',
  'badge': 'MCA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-computer-science',
  'department': 'department-of-computer-application',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'BCA / B.Sc in Computer Science / IT or a bachelor degree with Mathematics at '
                 '10+2 or graduation level, with a minimum of 50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


{'slug': 'bachelor-of-technology-data-science',
  'name': 'B.Tech in Data Science',
  'badge': 'Data Science',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-computer-science',
  'department': 'department-of-data-science',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': True,
  'eligibility': 'Passed 10+2 with Mathematics or Computer Science and a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


{'slug': 'master-of-science-data-science',
  'name': 'Master of Science in Data Science',
  'badge': 'Data Science',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-computer-science',
  'department': 'department-of-data-science',
  'program': 'post-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': True,
  'eligibility': 'Passed 10+2 with Mathematics or Computer Science and a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

{'slug': 'bsc-ancs',
  'name': 'B.SC(H) In Advanced Networking And Cyber Security',
  'badge': 'ancs',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-computer-science',
  'department': 'department-of-advanced-networking-cyber-security',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': True,
  'eligibility': 'Passed 10+2 with Mathematics or Computer Science and a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
{'slug': 'msc-ancs',
  'name': 'M.SC(H) In Advanced Networking And Cyber Security',
  'badge': 'ancs',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-computer-science',
  'department': 'department-of-advanced-networking-cyber-security',
  'program': 'post-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': True,
  'eligibility': 'Passed 10+2 with Mathematics or Computer Science and a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


{'slug': 'bsc-animation',
  'name': 'Bachelor of Science (Hons.) in Multimedia & Animation',
  'badge': 'animation',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-computer-science',
  'department': 'department-of-multimedia-animation',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': True,
  'eligibility': 'Passed 10+2 with Mathematics or Computer Science and a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


{'slug': 'msc-animation',
  'name': 'MSc in Multimedia and Animation',
  'badge': 'animation',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-computer-science',
  'department': 'department-of-multimedia-animation',
  'program': 'post-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': True,
  'eligibility': 'Passed 10+2 with Mathematics or Computer Science and a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


#computer application end

# math start
 {'slug': 'msc-in-mathematics',
  'name': 'Master of Science in Mathematics',
  'badge': 'M.Sc',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-basic-sciences',
  'department': 'department-of-mathematics',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 30,
  'is_featured': False,
  'eligibility': 'B.Sc with Mathematics as an honours or major subject, securing a minimum of '
                 '50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

# math end



# chem start

 {'slug': 'msc-in-chemestry',
  'name': 'Master of Science in Chemestry',
  'badge': 'M.Sc',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-basic-sciences',
  'department': 'department-of-chemistry',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 30,
  'is_featured': False,
  'eligibility': 'B.Sc with Mathematics as an honours or major subject, securing a minimum of '
                 '50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
# chem end

# phy start
{'slug': 'msc-in-physics',
  'name': 'Master of Science in physics',
  'badge': 'M.Sc',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-basic-sciences',
  'department': 'department-of-physics',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 30,
  'is_featured': False,
  'eligibility': 'B.Sc with Mathematics as an honours or major subject, securing a minimum of '
                 '50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

# phy end

#law start

 {'slug': 'ba-llb-honours',
  'name': 'B.A. LL.B. (Hons.)',
  'badge': 'BA LL.B',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-Legal-Studies',
  'department': 'department-of-legal-studies',
  'program': 'under-graduate',
  'duration': '5 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

 {'slug': 'bba-llb-honours',
  'name': 'BBA LL.B. (Hons.)',
  'badge': 'BBA LL.B',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-Legal-Studies',
  'department': 'department-of-legal-studies',
  'program': 'post-graduate',
  'duration': '1 Year',
  'total_seats': 30,
  'is_featured': False,
  'eligibility': 'LL.B or an equivalent law degree with a minimum of 50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

 {'slug': 'llb-honours',
  'name': 'LL.B.(Hons.)',
  'badge': 'LL.B',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-Legal-Studies',
  'department': 'department-of-legal-studies',
  'program': 'post-graduate',
  'duration': '1 Year',
  'total_seats': 30,
  'is_featured': False,
  'eligibility': 'LL.B or an equivalent law degree with a minimum of 50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
#law end


#optometry start

{'slug': 'bachelor-of-optometry',
  'name': 'Bachelor of Optometry',
  'badge': 'BA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-allied-health-services',
  'department': 'department-of-optometry',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


#optometry end


#food-nutriation start

{'slug': 'bachelor-of-Clinical-Nutrition-Dietetics',
  'name': 'B.Sc (H) in Clinical Nutrition & Dietetics',
  'badge': 'BSc',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-allied-health-services',
  'department': 'department-of-food-nutrition',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

{'slug': 'master-of-Food-Nutrition',
  'name': 'M.Sc in Food & Nutrition',
  'badge': 'MSc',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-allied-health-services',
  'department': 'department-of-food-nutrition',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},



#food-nutriation end


# bmlt start




{'slug': 'bachelor-of-science-medical-laboratory-technology',
  'name': 'Bachelor of Science (Hons.) in Medical Laboratory Technology',
  'badge': 'BA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-allied-health-services',
  'department': 'department-of-medical-laboratory-technology',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

# bmlt end



# bmrit start

{'slug': 'bachelor-of-medical-radiology-imaging-technology',
  'name': 'B.Sc. in Medical Radiology & Imaging Technology',
  'badge': 'BSc',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-allied-health-services',
  'department': 'department-of-medical-radiology-imaging-technology',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


# bmrit end

# english start

{'slug': 'ba-in-english',
  'name': 'Bachelor of Arts (B.A.) in English',
  'badge': 'BA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-humanities-social-science',
  'department': 'department-of-language-literature-cultural-studies',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


{'slug': 'ma-in-english',
  'name': 'Master of Arts (M.A.) in English',
  'badge': 'MA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-humanities-social-science',
  'department': 'department-of-language-literature-cultural-studies',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

{'slug': 'phd-in-english',
  'name': 'Doctor of Philosophy (Ph.D.) in English',
  'badge': 'phd',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-humanities-social-science',
  'department': 'department-of-language-literature-cultural-studies',
  'program': 'phd',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

#english end

# education start

{'slug': 'ba-in-education',
  'name': 'B.A (Hons.) in Education',
  'badge': 'BA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-humanities-social-science',
  'department': 'department-of-education',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


{'slug': 'ma-in-education',
  'name': 'M.A in Education',
  'badge': 'MA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-humanities-social-science',
  'department': 'department-of-education',
  'program': 'post-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

# education end

# agriculture start
{'slug': 'ba-in-agriculture',
  'name': ' B.Sc. (H) Agriculture',
  'badge': 'BA',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-agriculture',
  'department': 'department-of-agriculture',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},

{'slug': 'msc-in-agronomy',
  'name': ' M.Sc. (H) Agronomy',
  'badge': 'M.Sc.',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-agriculture',
  'department': 'department-of-agriculture',
  'program': 'post-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


{'slug': 'msc-in-soil-science',
  'name': ' M.Sc. (H) Soil Science',
  'badge': 'M.Sc.',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-agriculture',
  'department': 'department-of-agriculture',
  'program': 'post-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
{'slug': 'msc-in-genetics-plant-breedinge',
  'name': ' M.Sc. (H) Genetics & Plant Breedinge',
  'badge': 'M.Sc.',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-agriculture',
  'department': 'department-of-agriculture',
  'program': 'post-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
{'slug': 'msc-in-horticulture',
  'name': ' M.Sc. (H) Horticulture',
  'badge': 'M.Sc.',
  'card_image': '',
  'careers': [
      'Research Scientist',
      'Assistant Professor',
      'Principal Investigator',
      'Research and Development Lead',
  ],
  'school': 'school-of-agriculture',
  'department': 'department-of-agriculture',
  'program': 'post-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


# agriculture end










]

# --------------------------------------------------------------------------
# The tab panel on a course page  —  /academics/courses/<slug>/
#
#   KEY   = the course ``slug`` from COURSES above.
#   VALUE = the tabs, left to right. Same shape as DEPARTMENT_TABS:
#
#     title   the pill, and the heading above the panel unless 'heading' says
#             otherwise
#     icon    one of the symbols in templates/includes/icons.html, without the
#             "i-" prefix
#     intro   a paragraph above the list
#     points  [{'label': ..., 'text': ...}] — 'label' is optional, and a point
#             with only 'text' renders as a plain bullet
#     body    [paragraph, ...] for a tab that is prose rather than a list
#
# A course with NO entry here still gets a working panel: the view builds
# Programme Overview and Course Eligibility out of that course's own
# 'description' and 'eligibility'. Add a key here to say more than that.
COURSE_TABS = {
 'diploma-in-computer-science-technology': [
  {'title': 'Programme Overview',
   'icon': 'book',
   'intro': 'Upon completion of the diploma in computer science syllabus, graduates will be '
            'well-prepared to pursue higher studies in computer science or embark on a '
            'rewarding career in software development, systems analysis, web development or '
            'database administration.',
   'points': [
    {'text': 'Covers fundamental concepts and principles of computer science, including '
             'computer organization, data representation and digital logic.'},
    {'text': 'Students study multiple programming languages to develop a strong foundation in '
             'coding and software development.'},
    {'text': 'Focuses on the study and implementation of efficient data structure designs and '
             'algorithmic problem-solving techniques.'},
    {'text': 'Explores the fundamentals of network architecture, protocols and security, '
             'enabling students to understand the principles behind internet connectivity.'},
    {'text': 'Covers the complete software development life cycle, from requirements gathering '
             'to deployment, fostering skills in software design and project management.'},
    {'text': 'Introduces students to handling large sets of data efficiently and teaches them '
             'how to design and query databases effectively.'},
    {'text': 'Provides hands-on experience in web development, including HTML, CSS, JavaScript '
             'and server-side programming languages.'},
    {'text': 'Allows students to specialize in areas such as artificial intelligence, machine '
             'learning, cybersecurity or mobile application development.'},
   ]},

  {'title': 'Course Eligibility',
   'icon': 'scales',
   'intro': 'A candidate applying for this programme must meet all of the following:',
   'points': [
    {'text': 'Passed the secondary examination, or an equivalent, from a recognised board.'},
    {'text': 'A minimum of 35% marks in aggregate at that examination.'},
    {'text': 'English, Physical Science / Science and Mathematics must have been subjects '
             'at that examination.'},
   ]},

  {'title': 'Career Opportunities',
   'icon': 'industry',
   # 'slider' renders the points as a looping row of small cards - a picture
   # with the role under it - instead of a bulleted list. Drop this key and
   # the same points render as the list every other tab uses.
   'layout': 'slider',
   'intro': 'Roles this diploma leads into:',
   'points': [
    {'text': 'Software Engineer'},
    {'text': 'Hardware Engineer'},
    {'text': 'Networking Engineer'},
    {'text': 'Software Tester'},
    {'text': 'Web Designer'},
    {'text': 'App Developer'},
    {'text': 'Project Engineer'},
    {'text': 'IT Engineer'},
    {'text': 'Technical Support Engineer'},
    {'text': 'Voice Process Support Engineer'},
   ]},
 ],
}

# --------------------------------------------------------------------------
# Pictures for the Career Opportunities slider.
#
#   KEY   = the role exactly as it is written in 'careers' in COURSES, or in
#           the points of a Career Opportunities tab in COURSE_TABS.
#   VALUE = an image under static/, e.g. 'img/careers/software-engineer.jpg'.
#
# Keyed by role rather than by course because the roles repeat - "Software
# Engineer" appears under several programmes - so one picture here serves all
# of them. A role with no entry shows a plain icon instead of a broken image,
# which is why this can stay empty until the photographs are ready.
CAREER_IMAGES = {}

# --------------------------------------------------------------------------
# Frequently asked questions on a course page.
#
#   KEY   = the course ``slug``.  A course with no key here simply shows no
#           FAQ section, and the recruiter panel beside it widens to fill the
#           row - so a half-written page never looks broken.
COURSE_FAQS = {
 'diploma-in-computer-science-technology': [
  {'question': 'What subjects do Diploma in Computer Science and Technology students study '
               'during the course?',
   'answer': 'Students complete six semesters to earn the Computer Science and Technology '
             'diploma. The course categories are basic science, humanities and social science, '
             'engineering science and environmental science. Students also complete a summer '
             'internship in the third semester, and study computer programming, data '
             'structures and algorithms. The complete syllabus is on the website to download.'},
  {'question': 'What is the eligibility criterion to apply for a Diploma in Computer Science '
               'and Technology course at Swami Vivekananda University?',
   'answer': 'The candidate must have completed their secondary examination with a minimum of '
             '35% from a recognised board. The core subjects at that examination must be '
             'English, science and mathematics.'},
  {'question': 'What job roles can a Diploma in Computer Science and Technology graduate go '
               'for after college?',
   'answer': 'Roles to apply for after the diploma include hardware engineer, app developer, '
             'project engineer, IT engineer, technical support engineer and software engineer.'},
 ],
}

# --------------------------------------------------------------------------
# Board of Studies  —  the slider near the foot of a course page.
#
#   KEY   = the course ``slug``.  A course with no key here falls back to
#           DEFAULT_COURSE_BOARD below, so every course page carries the
#           section.  Add a key to give one course its own board.
#
#   Each row:
#     name         the line in bold. Put the member's name here once it is
#                  published; until then the seat is named instead, which is
#                  how a board is listed before it is filled.
#     designation  the role on the board, under the name
#     affiliation  the university, college or company, under that
#     photo        'img/board/somebody.jpg'. Leave it '' and the card shows a
#                  grey avatar rather than a broken image.
#
#   "{department}" in any of these is swapped for the course's own department
#   when the page renders, so one shared board reads correctly on every page.
COURSE_BOARD_OF_STUDIES = {}

# The board every course page shows unless COURSE_BOARD_OF_STUDIES names one
# for it. These are the SEATS on a Board of Studies, not people: a university
# publishes the composition first and the names as they are appointed. Replace
# 'name' with the member's name and add a 'photo' as each is confirmed -
# nothing in the template changes.
#
# The slider loops, so keep at least four here or the copies used to make the
# wrap seamless become obvious.
DEFAULT_COURSE_BOARD = [
    {'name': 'Head of the Department',
     'designation': 'Chairperson',
     'affiliation': '{department}, Swami Vivekananda University',
     'photo': ''},
    {'name': 'Dean of the School',
     'designation': 'Member',
     'affiliation': 'Swami Vivekananda University',
     'photo': ''},
    {'name': 'Senior Faculty Member',
     'designation': 'Member',
     'affiliation': '{department}, Swami Vivekananda University',
     'photo': ''},
    {'name': 'External Subject Expert',
     'designation': 'Member, nominated by the Academic Council',
     'affiliation': 'Invited from another university',
     'photo': ''},
    {'name': 'Industry Representative',
     'designation': 'Member, industry expert',
     'affiliation': 'From a partner organisation',
     'photo': ''},
    {'name': 'Alumni Representative',
     'designation': 'Member',
     'affiliation': 'Postgraduate alumnus of the department',
     'photo': ''},
    {'name': "Vice-Chancellor's Nominee",
     'designation': 'Member',
     'affiliation': 'Swami Vivekananda University',
     'photo': ''},
]

# --------------------------------------------------------------------------
FACILITIES = [{'slug': 'digital-library',
  'title': 'Digital Library',
  'image': 'img/facilities/12.jpg',
  'description': 'An online storehouse of textbooks, notes, journals, e-thesis, maps and rare '
                 'books.'},
 {'slug': 'smart-classrooms',
  'title': 'Smart Classrooms',
  'image': 'img/facilities/classroom.jpg',
  'description': 'Digital whiteboards make learning interactive across every lecture hall.'},
 {'slug': 'laboratories',
  'title': 'Laboratories',
  'image': 'img/facilities/lab.png',
  'description': 'Well-equipped engineering, science, pharmacy and nursing laboratories.'},
#  {'slug': 'hostel',
#   'title': 'Hostel',
#   'image': 'img/school-placeholder.svg',
#   'description': 'Separate, secure hostel accommodation for male and female students.'},
 {'slug': 'sports-complex',
  'title': 'Sports Complex',
  'image': 'img/facilities/sports.jpg',
  'description': 'Indoor and outdoor sporting facilities including a gymnasium.'},
#  {'slug': 'cafeteria',
#   'title': 'Cafeteria',
#   'image': 'img/school-placeholder.svg',
#   'description': 'Multi-cuisine cafeteria serving hygienic and affordable meals.'}
]

# --------------------------------------------------------------------------
# Appreciations  —  the vertical slider on the home page, beside the
# Chancellor's message, and the full page at /page/appreciations/.
#
# These six are the home slider: two on screen at a time, sliding one along
# every few seconds. Add or reorder rows to change which appear. The whole
# folder is static/img/appreciations/ and holds far more than six; the rest
# belong on the page behind View All, not here.
#
# The page behind View All is templates/pages/appreciations.html and is written
# by hand, so anything beyond these six goes straight into that template rather
# than into this list.
#
#   image     path under static/
#   alt_text  what the certificate or photograph shows. It is the only
#             description for anyone who cannot see it, so say what is in the
#             frame rather than repeating the word "appreciation".
#
# TODO: every alt_text below is the same generic line, because the images
# could not be opened here to read them. The file names look like people's
# names, so each is probably an appreciation from a named person - write
# that in and the slider becomes describable to anyone who cannot see it.
APPRECIATIONS = [
 {'image': 'img/appreciations/TANMOY.jpeg',
  'alt_text': 'An appreciation received by Swami Vivekananda University'},
 {'image': 'img/appreciations/abhay_jere.png',
  'alt_text': 'An appreciation received by Swami Vivekananda University'},
 {'image': 'img/appreciations/abhishek.png',
  'alt_text': 'An appreciation received by Swami Vivekananda University'},
 {'image': 'img/appreciations/alanriach.png',
  'alt_text': 'An appreciation received by Swami Vivekananda University'},
 {'image': 'img/appreciations/amrit-sen.avif',
  'alt_text': 'An appreciation received by Swami Vivekananda University'},
 {'image': 'img/appreciations/anirudh.png',
  'alt_text': 'An appreciation received by Swami Vivekananda University'}]

# --------------------------------------------------------------------------
# The counting figures under the video carousel.
#
# TODO: every value is 0. Put the real figures in before this goes in front of
# anyone — these are published as statements of fact about the university, so
# they should come from someone who knows them rather than be guessed at. The
# section hides itself while the list is empty, but NOT while the values are
# zero, so zeros will show if they are left here.
#
#   value    the number to count up to. Plain int or float, no commas and no
#            "+" — the separator is added while counting and the suffix is its
#            own field, so 8500 renders as 8,500+
#   suffix   drawn after the number and never animated: '+', '%', 'k', or ''
#   label    the caption under it
#
# Four across on a wide screen, so a count that is a multiple of four leaves no
# orphan at the end of the row.
STATS = [
 {'value': 200, 'suffix': '+', 'label': 'Industry Collaborations'},
 {'value': 50, 'suffix': '+', 'label': 'International MoUs'},
 {'value': 500, 'suffix': '+', 'label': 'Patents Filed'},
 {'value': 60, 'suffix': '+', 'label': 'Programs Offered'},
 {'value': 3000, 'suffix': '+', 'label': 'Alumni Network'},
 {'value': 15000, 'suffix': '+', 'label': 'Current Student'},

 ]

# --------------------------------------------------------------------------
# Life at SVU — the eight-tile photo grid on the home page, and the eight pages
# behind it (templates/pages/life/<slug>.html, routed by views.life_detail).
#
# Order is the reading order of the grid: four across on a wide screen, read
# left to right, top row then bottom. Keep the count a multiple of four and no
# row is ever left short.
#
# ON THE PHOTOGRAPHS
#   All eight are real photographs now. The alt text below was written from
#   the subject each file was given rather than from the picture itself, so
#   check it says what is actually in the frame: it is the only description
#   anyone using the page by ear will get. 'placeholder': True marks a tile
#   still waiting for artwork; none are, at present.
#
# alt_text is not decorative. It is the only description of the picture for
# anyone who cannot see it, so write what is in the frame rather than repeating
# the title — "Sports" is not a description of a volleyball match.
LIFE_AT_SVU = [
 {'slug': 'library',
  'title': 'Library',
  'image': 'img/facilities/12.jpg',
  'alt_text': 'Students at the shelves in the university library',
  'placeholder': False},
 {'slug': 'laboratory',
  'title': 'Laboratory',
  'image': 'img/facilities/lab.png',
  'alt_text': 'Students working at the benches in a university laboratory',
  'placeholder': False},
 {'slug': 'classroom',
  'title': 'Classroom',
  'image': 'img/facilities/classroom.jpg',
  'alt_text': 'A class in progress in one of the lecture rooms',
  'placeholder': False},
 {'slug': 'campus-building',
  'title': 'Campus Building',
  'image': 'img/about/campus.jpg',
  'alt_text': 'The Barrackpore campus, with the WE LOVE SVU installation on the lawn',
  'placeholder': False},
 {'slug': 'gardening',
  'title': 'Gardening',
  'image': 'img/facilities/garden.jpg',
  'alt_text': 'Students and staff tending the flower beds on campus',
  'placeholder': False},
 {'slug': 'sports',
  'title': 'Sports',
  'image': 'img/facilities/sports.jpg',
  'alt_text': 'A match under way on the campus sports ground',
  'placeholder': False},
 {'slug': 'group-study',
  'title': 'Group Study',
  'image': 'img/facilities/groupstudy.jpg',
  'alt_text': 'Students working through a text together',
  'placeholder': False},
 {'slug': 'practical-laboratory',
  'title': 'Practical Laboratory',
  'image': 'img/facilities/lab-2.jpg',
  'alt_text': 'Bench work under supervision in a practical laboratory',
  'placeholder': False}]

# --------------------------------------------------------------------------
PARTNERS = [{'name': 'Tata Consultancy Services', 'logo': 'img/partners/partner-1.png', 'url': ''},
 {'name': 'Wipro', 'logo': 'img/partners/partner-2.png', 'url': ''},
 {'name': 'Cognizant', 'logo': 'img/partners/partner-3.png', 'url': ''},
 {'name': 'Capgemini', 'logo': 'img/partners/partner-4.png', 'url': ''},
 {'name': 'Tech Mahindra', 'logo': 'img/partners/partner-5.png', 'url': ''},
 {'name': 'ITC Infotech', 'logo': 'img/partners/partner-6.png', 'url': ''},
 {'name': 'Byjus', 'logo': 'img/partners/partner-7.png', 'url': ''},
 {'name': 'Reliance Retail', 'logo': 'img/partners/partner-8.png', 'url': ''}]

# --------------------------------------------------------------------------
# Events and notices
EVENTS = [

    {
    'slug': 'swami-vivekananda-university-celebrated-the-80th-independence-day-on-campus',
    'title': 'Swami Vivekananda University celebrated the 80th Independence Day on campus with patriotic fervour',
    'event_date': '2026-08-15',
    'venue': 'SVU Campus, Barrackpore, Kolkata',
    'excerpt': 'Swami Vivekananda University celebrated the 80th Independence Day on campus with patriotic fervour. The ceremony featured the unfurling of the national flag, an NCC parade, cultural performances and patriotic activities by students and cadets. The programme saw…',
    'description': '<p>Swami Vivekananda University celebrated the 80th Independence Day on campus with patriotic fervour and enthusiasm. The ceremony featured the unfurling of the national flag, an NCC parade, cultural performances and patriotic activities by students and cadets.</p><p>The programme saw enthusiastic participation from students, faculty members, staff and invited guests from across the university. The celebrations highlighted the values of freedom, unity, patriotism and the responsibilities of the nation’s youth.</p>',
    'cover_image': 'img/events/1.jfif',
    'alt_text': 'Swami Vivekananda University celebrated the 80th Independence Day on campus with patriotic fervour, featuring flag hoisting, NCC parade and cultural performances',
    'is_featured': True,
},


{
    'slug': 'swami-vivekananda-university-observed-14th-august-as-a-day-of-remembrance',
    'title': '14th August – A Day of Remembrance " Har Ghar Tiranga" ',
    'event_date': '2026-08-14',
    'venue': 'SVU Campus, Barrackpore, Kolkata',
    'excerpt': 'Swami Vivekananda University, in collaboration with NSS, observed 14th August as a Day of Remembrance, reflecting on the Partition of the Nation and its impact on West Bengal. The programme remembered the past, honoured those who suffered, and inspired a future of peace, unity, and humanity.',
    'description': '<p>Swami Vivekananda University, in collaboration with NSS, observed 14th August as a Day of Remembrance, reflecting on the Partition of the Nation and its impact on West Bengal.</p><p>The programme provided a solemn moment to remember the past, honour those who suffered, and inspire a future rooted in peace, unity, and humanity.</p><p><strong>“Remembering the Past... Honouring the Suffering... Inspiring the Future.”</strong></p><p>The observance was also aligned with the <strong>Har Ghar Tiranga</strong> initiative, encouraging the spirit of patriotism and national unity among students and members of the university community.</p>',
    'cover_image': 'img/events/2.jpg',
    'alt_text': 'Swami Vivekananda University observed 14th August as a Day of Remembrance in collaboration with NSS, reflecting on the Partition of the Nation and its impact on West Bengal',
    'is_featured': True,
},




 {
    'slug': 'swami-vivekananda-university-hosted-smart-india-hackathon-2026',
    'title': 'Swami Vivekananda University hosted Smart India Hackathon 2026',
    'event_date': '2026-08-07',
    'venue': 'SVU Campus, New Town, Kolkata',
    'excerpt': 'Swami Vivekananda University proudly participated in Smart India Hackathon 2026, bringing together talented students, mentors and faculty members to develop innovative solutions to real-world challenges.',
    'description': '<p>Swami Vivekananda University proudly participated in <strong>Smart India Hackathon 2026</strong>, providing students with an exciting platform to showcase their creativity, technical skills and innovative thinking.</p><p>The event brought together talented students, faculty members and mentors who collaborated to develop technology-driven solutions to real-world challenges. The programme encouraged teamwork, problem-solving, innovation and entrepreneurship among the participants.</p><p>The initiative reflected SVU’s commitment to fostering a culture of innovation and empowering students to contribute meaningful solutions for a smarter and more developed India.</p>',
    'cover_image': 'img/events/3.jfif',
    'alt_text': 'Swami Vivekananda University participated in Smart India Hackathon 2026 with students, mentors and faculty members showcasing innovative solutions',
    'is_featured': True,
},



#  {'slug': 'swami-vivekananda-university-one-of-the-eastern-indias-leading-multidi',
#   'title': 'SVU has entered into a strategic collaboration with GreenAI Services Pvt. Ltd.',
#   'event_date': '2026-06-22',
#   'venue': 'SVU Campus, New Town, Kolkata',
#   'excerpt': "Swami Vivekananda University, one of the Eastern India's leading "
#              'multidisciplinary universities, has entered into a strategic collaboration with '
#              'Greenax Services Pvt. Ltd.The programme saw enthusiastic participation from '
#              'students, faculty members…',
#   'description': "<p>Swami Vivekananda University, one of the Eastern India's leading "
#                  'multidisciplinary universities, has entered into a strategic collaboration '
#                  'with Greenax Services Pvt. Ltd.</p><p>The programme saw enthusiastic '
#                  'participation from students, faculty members and invited guests across '
#                  'departments.</p>',
#   'cover_image': 'img/events/event-4.jpg',
#   'alt_text': "Swami Vivekananda University, one of the Eastern India's leading "
#               'multidisciplinary universities, has entered into a strategic collaboration with '
#               'Greenax Service',
#   'is_featured': False},
#  {'slug': 'swami-vivekananda-university-had-the-privilege-of-hosting-an-exclusive',
#   'title': 'SVU hosted an exclusive session with H.E. Mr. Bishnu Prasad Gautam, Ambassador of '
#            'Nepal to India',
#   'event_date': '2026-06-07',
#   'venue': 'SVU Campus, New Town, Kolkata',
#   'excerpt': 'Swami Vivekananda University had the privilege of hosting an exclusive session '
#              'with H.E. Mr. Bishnu Prasad Gautam, Ambassador of Nepal to IndiaThe programme '
#              'saw enthusiastic participation from students, faculty members…',
#   'description': '<p>Swami Vivekananda University had the privilege of hosting an exclusive '
#                  'session with H.E. Mr. Bishnu Prasad Gautam, Ambassador of Nepal to '
#                  'India</p><p>The programme saw enthusiastic participation from students, '
#                  'faculty members and invited guests across departments.</p>',
#   'cover_image': 'img/events/event-5.jpg',
#   'alt_text': 'Swami Vivekananda University had the privilege of hosting an exclusive session '
#               'with H.E. Mr. Bishnu Prasad Gautam, Ambassador of Nepal to India',
#   'is_featured': False},
#  {'slug': 'upcoming-event-faculty-development-programme-organised-by-department-o',
#   'title': 'Faculty Development Programme on Intersectionality: Beyond Single-Axis Thinking',
#   'event_date': '2026-05-24',
#   'venue': 'SVU Campus, New Town, Kolkata',
#   'excerpt': 'Upcoming event — Faculty development programme organised by Department of '
#              'Sociology: SVU Intersectionality on methods beyond singles — Axis thinkingThe '
#              'programme saw enthusiastic participation from students, faculty members and '
#              'invited…',
#   'description': '<p>Upcoming event — Faculty development programme organised by Department of '
#                  'Sociology: SVU Intersectionality on methods beyond singles — Axis '
#                  'thinking</p><p>The programme saw enthusiastic participation from students, '
#                  'faculty members and invited guests across departments.</p>',
#   'cover_image': 'img/events/event-6.jpg',
#   'alt_text': 'Upcoming event — Faculty development programme organised by Department of '
#               'Sociology: SVU Intersectionality on methods beyond singles — Axis thinking',
#   'is_featured': False},
#  {'slug': 'convocation-2026-swami-vivekananda-university-confers-degrees-on-the-g',
#   'title': 'Convocation 2026 - SVU confers degrees on the graduating batch across all schools',
#   'event_date': '2026-05-12',
#   'venue': 'SVU Campus, New Town, Kolkata',
#   'excerpt': 'Convocation 2026 — Swami Vivekananda University confers degrees on the '
#              'graduating batch across all schoolsThe programme saw enthusiastic participation '
#              'from students, faculty members and invited guests across departments.',
#   'description': '<p>Convocation 2026 — Swami Vivekananda University confers degrees on the '
#                  'graduating batch across all schools</p><p>The programme saw enthusiastic '
#                  'participation from students, faculty members and invited guests across '
#                  'departments.</p>',
#   'cover_image': 'img/events/event-7.jpg',
#   'alt_text': 'Convocation 2026 — Swami Vivekananda University confers degrees on the '
#               'graduating batch across all schools',
#   'is_featured': False}
]

# --------------------------------------------------------------------------
# Notices  —  /notices/ and /notices/<slug>/
#
#   slug          the address. Changing it changes the URL and breaks any link
#                 already pointing at the notice.
#   date          'YYYY-MM-DD'. The list is sorted on this, newest first.
#   title         shown on the board, the list and the notice itself
#   is_important  puts the red NEW flag beside it and sets the title in bold
#   body          the text of the notice
#
# ATTACHING A PDF  —  both of these are optional; leave them out for a notice
# that is only text.
#
#   document        path under static/, e.g. 'documents/exam-revision.pdf'.
#                   A full https:// address works too and is passed straight
#                   through. The notice page turns it into a button and the
#                   list marks the row PDF.
#   document_label  the wording on that button. Defaults to
#                   "Download the notice (PDF)".
#
#   Put the file in static/documents/ and run:
#       python manage.py collectstatic --noinput
#   A path with no manifest entry would normally take the page down with a
#   ValueError; here it does not. The view resolves it the forgiving way, so a
#   mistyped path costs the attachment and logs a warning rather than losing
#   the notice.
#
#   {'slug': 'exam-revision',
#    'date': '2026-05-23',
#    'title': 'Revision of the examination schedule',
#    'is_important': True,
#    'body': 'The revised schedule is attached.',
#    'document': 'documents/exam-revision.pdf',
#    'document_label': 'Revised schedule (PDF)'},
NOTICES = [{'slug': 'revision-of-examination-date-id-ud-zoha',
  'date': '2026-05-23',
  'title': 'Notification - Revision of Date of Examination due to change in date of holiday on '
           'account of Id-Ud-Zoha (Bakrid)',
  'is_important': True,
  'body': 'All students are informed that the date of the end-semester examination has been '
          'revised following the change in the date of the holiday on account of Id-Ud-Zoha '
          '(Bakrid). The revised schedule is available with the Controller of Examinations.'},




 {'slug': 'change-in-date-of-holiday-id-ud-zoha',
  'date': '2026-05-23',
  'title': 'Notice - Change in date of holiday on account of Id-Ud-Zoha (Bakrid)',
  'is_important': True,
  'body': 'The holiday on account of Id-Ud-Zoha (Bakrid) has been rescheduled. The campus will '
          'remain closed on the revised date and all classes stand adjusted accordingly.'},
 {'slug': 'result-of-university-cafeteria-design-competition',
  'date': '2026-05-15',
  'title': 'Result of University Cafeteria Design Competition',
  'is_important': False,
  'body': 'The results of the University Cafeteria Design Competition have been declared. '
          'Winners may collect their certificates from the Students Welfare Office.'},
 {'slug': 'notice-for-semester-registration-2026-27',
  'date': '2026-05-06',
  'title': 'Notice for semester registration for the academic session 2026-27',
  'is_important': False,
  'body': 'Semester registration for the academic session 2026-27 is now open. Students must '
          'complete registration through the student portal before the last date to avoid a '
          'late fee.'},
 {'slug': 'schedule-for-supplementary-examination',
  'date': '2026-04-28',
  'title': 'Schedule for supplementary examination - even semester',
  'is_important': False,
  'body': 'The schedule for the even-semester supplementary examination has been published. '
          'Admit cards will be issued one week before the commencement of the examination.'},
 {'slug': 'anti-ragging-undertaking-mandatory',
  'date': '2026-04-11',
  'title': 'Submission of anti-ragging undertaking is mandatory for all students',
  'is_important': True,
  'body': 'Every student and parent must submit the online anti-ragging undertaking as '
          'mandated by the UGC. Non-submission will hold up semester registration.'},
 {'slug': 'library-membership-renewal',
  'date': '2026-03-30',
  'title': 'Library membership renewal for the new academic session',
  'is_important': False,
  'body': 'Library membership for continuing students must be renewed at the circulation desk. '
          'Digital library credentials will be reissued after renewal.'},
 {'slug': 'notice-for-summer-internship-2026',
  'date': '2026-03-18',
  'title': 'Notice for summer internship 2026 - registration through the placement cell',
  'is_important': False,
  'body': 'Pre-final year students may register with the Training & Placement Cell for the '
          'summer internship drive. Registration closes at the end of the month.'}]

# --------------------------------------------------------------------------
# Admission
ADMISSION_STEPS = [{'title': 'Fill the enquiry form',
  'description': 'Share your details and programme of interest so our admission counsellors '
                 'can reach you.'},
 {'title': 'Submit your application',
  'description': 'Complete the online application form and upload your academic documents.'},
 {'title': 'Counselling & document verification',
  'description': 'Attend the counselling session; original documents are verified at this '
                 'stage.'},
 {'title': 'Pay the fee and confirm your seat',
  'description': 'Pay the admission fee online to confirm your seat and receive your enrolment '
                 'number.'}]

# --------------------------------------------------------------------------
SCHOLARSHIPS = [{'title': 'Merit Scholarship',
  'description': 'Awarded on the basis of qualifying examination marks and entrance '
                 'performance.',
  'percentage': 'Up to 100%',
  'criteria': ''},
 {'title': 'University Scholarship Foundation Award',
  'description': 'For meritorious students under special categories including single girl '
                 'child, wards of defence personnel and differently-abled applicants.',
  'percentage': 'Special categories',
  'criteria': ''},
 {'title': 'Sports Scholarship',
  'description': 'For students representing the state or country in recognised sporting '
                 'events.',
  'percentage': 'Up to 50%',
  'criteria': ''}]

# --------------------------------------------------------------------------
STATES = ['Assam',
 'Bihar',
 'Delhi',
 'Gujarat',
 'Haryana',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Madhya Pradesh',
 'Maharashtra',
 'Meghalaya',
 'Odisha',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'West Bengal']

# --------------------------------------------------------------------------
CITIES = {'Assam': ['Dibrugarh', 'Guwahati', 'Jorhat', 'Silchar'],
 'Bihar': ['Bhagalpur', 'Gaya', 'Muzaffarpur', 'Patna'],
 'Delhi': ['Dwarka', 'New Delhi', 'Rohini'],
 'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara'],
 'Haryana': ['Faridabad', 'Gurugram', 'Panipat'],
 'Jharkhand': ['Bokaro', 'Dhanbad', 'Jamshedpur', 'Ranchi'],
 'Karnataka': ['Bengaluru', 'Mangaluru', 'Mysuru'],
 'Kerala': ['Kochi', 'Kozhikode', 'Thiruvananthapuram'],
 'Madhya Pradesh': ['Bhopal', 'Indore', 'Jabalpur'],
 'Maharashtra': ['Mumbai', 'Nagpur', 'Nashik', 'Pune'],
 'Meghalaya': ['Shillong', 'Tura'],
 'Odisha': ['Bhubaneswar', 'Cuttack', 'Puri', 'Rourkela'],
 'Punjab': ['Amritsar', 'Chandigarh', 'Ludhiana'],
 'Rajasthan': ['Jaipur', 'Jodhpur', 'Udaipur'],
 'Sikkim': ['Gangtok', 'Namchi'],
 'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai'],
 'Telangana': ['Hyderabad', 'Warangal'],
 'Tripura': ['Agartala', 'Udaipur'],
 'Uttar Pradesh': ['Ghaziabad', 'Kanpur', 'Lucknow', 'Noida', 'Varanasi'],
 'West Bengal': ['Asansol',
                 'Barasat',
                 'Durgapur',
                 'Howrah',
                 'Kharagpur',
                 'Kolkata',
                 'Siliguri']}

# --------------------------------------------------------------------------
# Static pages
FAQS = [{'question': 'When do admissions for 2026-27 open?',
  'answer': 'Admissions for the 2026-27 session are open now. Apply online or call our '
            'admission helpline.',
  'category': 'Admission'},
 {'question': 'Does SVU take admission through agents or consultants?',
  'answer': 'No. SVU does not take admission through any agents or consultants. Please '
            'refer to the SVU website only for any admission-related query.',
  'category': 'Admission'},
 {'question': 'What entrance exams does SVU accept?',
  'answer': 'NET for MBA, WEBJEE and JEE Main for B.TECH, CLAT for law programmes.',
  'category': 'Admission'},
 {'question': 'Are scholarships available?',
  'answer': 'Yes — merit scholarships of up to 100% are offered, along with '
            'special-category scholarships from the University Scholarship Foundation.',
  'category': 'Fees & Scholarships'},
 {'question': 'Is hostel accommodation available?',
  'answer': 'Yes, separate hostel accommodation is available for male and female students '
            'with 24x7 security and dining facilities.',
  'category': 'Campus'},
 {'question': 'What is the highest placement package?',
  'answer': 'The highest placement package recorded is 25 LPA.',
  'category': 'Placements'}]

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# 'about-svu' is deliberately absent: About Us has its own template and view
# (templates/pages/about.html), so it is not rendered from this dict.
#
# 'chancellors-message' is absent for the same reason — it has its own page
# (templates/pages/chancellors_message.html) built from the CHANCELLOR dict
# further up this file.  Edit CHANCELLOR['full_message'] to change that text;
# an entry here would simply be ignored, since the dedicated URL matches first.
PAGES = {'privacy-policy': {'title': 'Privacy Policy',
                    'subtitle': '',
                    'content': '<h2>What we collect</h2><p>When you submit the enquiry or '
                               'contact form we collect your name, e-mail address, mobile '
                               'number, location and programme of interest, along with your '
                               'consent record, the page you submitted from, your IP address '
                               'and browser user-agent. The last three are kept purely as an '
                               'anti-abuse audit trail.</p><h2>Why we collect it</h2><p>Solely '
                               'to respond to your admission enquiry. We never sell your data '
                               'and never share it with third-party marketers.</p><h2>How long '
                               'we keep it</h2><p>Enquiries and contact messages are '
                               'automatically purged after 24 months.</p><h2>Cookies</h2><p>We '
                               'set only a session cookie and a CSRF cookie — both are '
                               'strictly necessary for the site to work securely. We run no '
                               'third-party advertising or analytics cookies.</p><h2>Your '
                               'rights</h2><p>Write to us to access, correct or delete the '
                               'personal data we hold about you.</p>'},
 'terms-conditions': {'title': 'Terms & Conditions',
                      'subtitle': '',
                      'content': '<p>By using this website you agree to use it lawfully and '
                                 'not to attempt to gain unauthorised access to any part of '
                                 'it. Content is the property of Swami Vivekananda University '
                                 'unless stated otherwise.</p>'},
 'fee-refund-policy': {'title': 'Fee Refund Policy',
                       'subtitle': '',
                       'content': '<p>Fee refunds are processed in line with the UGC refund '
                                  'policy notification. Applications for refund must be '
                                  'submitted in writing to the Accounts Department.</p>'},
 # Kept for the site search, which walks PAGES. The page itself is served by
 # views.ugc_compliance from templates/pages/ugc_compliance.html now, so this
 # 'content' is the search excerpt rather than what anybody reads on the page.
 'ugc-compliance': {'title': 'UGC Compliance Documents',
                    'subtitle': '',
                    'content': '<p>Statutory documents and disclosures mandated by the '
                               'University Grants Commission are published on this page.</p>'},
 'public-self-disclosure': {'title': 'Public Self-Disclosure',
                            'subtitle': '',
                            'content': '<p>Institutional information published under the UGC '
                                       'public self-disclosure requirement.</p>'},
 'scholarships': {'title': 'Scholarships',
                  'subtitle': '',
                  'content': '<p>The University Scholarship Foundation offers scholarships to '
                             'meritorious students under special categories. Merit '
                             'scholarships of up to 100% are available.</p>'},
 'iqac': {'title': 'IQAC',
          'subtitle': '',
          'content': '<p>The Internal Quality Assurance Cell (IQAC) works towards continuous '
                     'improvement of the academic and administrative performance of the '
                     'university.</p>'},
 'nirf': {'title': 'NIRF',
          'subtitle': '',
          'content': '<p>National Institutional Ranking Framework data templates and '
                     'submissions.</p>'},
 'wilp': {'title': 'WILP',
          'subtitle': '',
          'content': '<p>The Work Integrated Learning Programme (WILP) allows working '
                     'professionals to pursue a degree alongside employment.</p>'},
 'anti-ragging': {'title': 'Anti-Ragging Committee',
                  'subtitle': '',
                  'content': '<p>Swami Vivekananda University maintains a strict '
                             'zero-tolerance policy on ragging. The Anti-Ragging Committee and '
                             'Squad monitor the campus and hostels continuously.</p>'}}

# --------------------------------------------------------------------------
# Leadership and administration, shown on /page/our-team/ as one scroll-
# stacked panel per person. Ported from the earlier build. Photos live in
# static/img/our_team/ and were renamed to clean slugs on the way in.
TEAM = [{'name': 'Dr. Nandan Gupta',
  'role': 'Chancellor',
  'photo': 'img/our_team/nandan-gupta.png',
  'messages': ['I welcome everyone at Swami Vivekananda University. The essential information '
               'of this esteemed setup is available in this website. Since its inception, SVU '
               'has made rapid strides both in the area of academics and research. The '
               'emergence and reputation of SVU in various spheres of academia and industry '
               'reflects this rapid growth. The website has been carrying the chronological '
               'information. The inception years were really challenging due to pandemic, '
               'however, resilience shown by the staff and students helped the university in '
               'tiding over the difficult situation. I am hopeful that the SVU will match up '
               'to the societal expectation in a demand driven way. I wish SVU all success in '
               'future.']},
 {'name': 'Dr. Ashok Binaykia',
  'role': 'Trustee Member',
  'photo': 'img/our_team/ashok-binaykia.jpg',
  'messages': ['It gives me immense pleasure to welcome you all to Swami Vivekananda '
               'University. Since its establishment, the University has been committed to '
               'achieving excellence in academics, research, and innovation. Our journey, '
               'though filled with challenges, especially during the unprecedented pandemic '
               'years, has been marked by resilience, determination, and growth. The '
               'collective efforts of our faculty, staff, and students have enabled SVU to '
               'carve a niche in higher education and gain recognition across academic and '
               'professional domains. This website serves as a comprehensive source of '
               'information about our vision, mission, programs, and achievements. I firmly '
               'believe that SVU will continue to contribute meaningfully to society and '
               'fulfill the expectations of our stakeholders.']},
 {'name': 'Dr. Rakesh Binaykia',
  'role': 'Pro-Chancellor',
  'photo': 'img/our_team/rakesh-binaykia.jpg',
  'messages': ['A warm welcome to everyone visiting the official website of Swami Vivekananda '
               'University. The University stands as a symbol of knowledge, growth, and '
               'innovation, fostering both academic and research excellence. From its '
               'formative years, SVU has faced and overcome challenges with determination, '
               'particularly during the pandemic, which tested our adaptability and '
               'resilience. The steady progress made in a short span of time reflects the '
               'dedication of our faculty and the enthusiasm of our students. This platform '
               'offers detailed insights into our initiatives, programs, and accomplishments. '
               'Looking ahead, I am confident that SVU will continue to evolve as a dynamic '
               'center of learning and meet the aspirations of society in a progressive '
               'manner.']},
 {'name': 'Mr. Chandan Gupta',
  'role': 'Trustee Member',
  'photo': 'img/our_team/chandan-gupta.jpg',
  'messages': ['It gives me immense pride and joy to be associated with Swami Vivekananda '
               'University, an institution inspired by the ideals and vision of Swami '
               'Vivekananda. The University stands as a beacon of knowledge, discipline, and '
               'values, preparing young minds not only for successful careers but also for '
               'meaningful lives of service to society.',
               'Our aim is to nurture students who are intellectually competent, morally '
               'upright, socially responsible, and globally aware. In this rapidly changing '
               'world, we are committed to providing an education that blends academic '
               'excellence with innovation, research, and holistic development.',
               'I firmly believe that education should not be limited to classrooms—it should '
               'empower individuals to face challenges with confidence, compassion, and '
               'integrity. At Swami Vivekananda University, we strive to instill these values '
               'in every student, shaping them into leaders of tomorrow.',
               'I welcome all students, faculty, and well-wishers to be a part of this journey '
               'of growth, discovery, and transformation. Together, let us uphold the noble '
               'vision of Swami Vivekananda and contribute towards building a better future '
               'for our nation and the world.']},
 {'name': 'Prof.(Dr.) Shorosimohan Dan',
  'role': 'Chief Mentor',
  'photo': 'img/our_team/shorosimohan-dan.png',
  'messages': ['“Arise, awake and stop not until the goal is achieved”',
               'Swami Vivekananda University is the brain child and dream project of Dr. '
               'Nandan Gupta, a scholar par excellence and great visionary, and his team. '
               'Since inception they left no stone unturned to make it a State-of the-Art '
               'institute. As a result, the University has made remarkable progress in areas '
               'of teaching, research and co-curricular activities within a very short period '
               'although it started its journey during covid pandemic period. Laboratories are '
               'equipped with latest and required equipments. Spectacular civil infrastructure '
               'is drawing attention of the passersby. The University is well connected with '
               'the metros and cities having reputed educational institutions through rail and '
               'roads, although its location is away from the hassle and bustle of the city.',
               '21st century has been proclaimed as the knowledge century era. Students build '
               'themselves into knowledge society by understanding the advancement of '
               'frontiers of knowledge. For that matter digital transformation is our dream. '
               'Artificial Intelligence will certainly play a vital role in the days to come.',
               'Now ‘The world is flat. The playing field is being leveled today.’ Swami '
               'Vivekananda University is all set &well prepared to take advantage of it to '
               'face the challenges ahead of it by infusing new blood in every sphere of its '
               'activities.',
               'I am indeed privileged and honoured to be associated with this esteemed '
               'organization.']},
 {'name': 'Prof. (Dr.) Subrata Kumar Dey',
  'role': 'Vice Chancellor',
  'photo': 'img/our_team/subrata-kumar-dey.png',
  'messages': ["It's indeed a privilege to be at the forefront of an emerging university, our "
               'SVU. It is a matter of pride and satisfaction that ever since its inception in '
               '2020, SVU has been striving for excellence in Higher Education, Research, and '
               'Extension activities. Gratitude to the guidance of the honorable Chancellor '
               "and thanks to the efforts of our Colleagues, the University's Undergraduate, "
               'Postgraduate, and Doctoral Programs in the areas of Engineering, Management, '
               'Agriculture, Computer Science, Life Sciences, Allied Health Science, '
               'Humanities, and Social Sciences. I extend my gratitude to all associated with '
               'the website built and the coordination works, even during this challenging '
               'phase of the global pandemic. I wish that our university continues to focus on '
               'the student-centric education delivery processes.']},
 {'name': 'Prof. (Dr.) Apurba Ratan Ghosh',
  'role': 'Pro-Vice Chancellor',
  'photo': 'img/our_team/apurba-ratan-ghosh.png',
  'messages': ['Swami Vivekananda University stands today as one of the fastest-growing and '
               'most promising institutions of higher education in Eastern India. Since its '
               'establishment in 2019, the University has remained steadfast in its commitment '
               'to transforming the aspirations of young minds into meaningful achievements '
               'through quality education, academic excellence, innovation, research, skill '
               'development, and social advancement. Inspired by the timeless ideals of Swami '
               'Vivekananda, we endeavour to cultivate not only knowledge but also character, '
               'creativity, compassion, and leadership among our students.',
               'At Swami Vivekananda University, we provide a vibrant and intellectually '
               'stimulating learning environment that fosters interdisciplinary education, '
               'cutting-edge research, innovation, entrepreneurship, and ethical values. Our '
               'state-of-the-art infrastructure, advanced laboratories, digital learning '
               'resources, and industry-oriented programmes are designed to equip students '
               'with the competencies required in an increasingly dynamic and '
               'technology-driven world.',
               'A diverse range of academic programmes aligned with the National Education '
               'Policy (NEP 2020) and contemporary global trends, we prepare our students to '
               'become competent professionals, responsible citizens, and lifelong learners '
               'capable of addressing the challenges of the twenty-first century. Guided by '
               'our vision of becoming a globally respected centre of learning, research, and '
               'innovation, and driven by our mission to achieve excellence in academics, '
               'research, innovation, and community engagement, we continue to strengthen our '
               'contributions to society through knowledge creation and dissemination.',
               'As Pro-Vice Chancellor, I am deeply committed to enhancing academic quality, '
               'promoting research excellence, fostering inclusivity and equity, advancing '
               'sustainability, and ensuring the continued growth and development of our '
               'institution. I warmly invite students, parents, researchers, industry '
               'partners, alumni, and well-wishers to join us in our collective journey '
               'towards knowledge, innovation, and excellence.',
               'Together, let us uphold the inspiring ideal: “Vasudhaiva Kutumbakam: Global '
               'Learning, Shared Humanity, Sustainable Future.”']},
 {'name': 'Prof. (Dr.)Deb Narayan Bandyopadhyay',
  'role': 'Chief Executive Director(Academics)',
  'photo': 'img/our_team/deb-narayan-bandyopadhyay.png',
  'messages': ["In consonance with Swami Vivekananda University's avowed assertion to build "
               'bridges between academic intellect and professional efficiency, our university '
               'aspires to stride across a wider spectrum of knowledge dissemination. With '
               'this specific vision, this university intends to move beyond the regional and '
               'the national and foreshadow a new academic destiny by participating in a '
               'global society.',
               'Swami Vivekananda University is already in the process of using the expertise '
               'of the British Council, American Centre (USEFI) and the Australian Consulate. '
               'Our university has already signed the MoU with the Scottish Centre of Tagore '
               'Studies (Scotland). Moreover, universities like the Universitat Rovira I '
               'Virgili ( Spain), University of Lodz (Poland), University of East London have '
               'shown interest in exploring more possibilities in terms of student and staff '
               'mobility. Some key members of the university were recently invited to a '
               'high-level meeting on academic exchanges at the Australian Consulate to share '
               'their views with Mr Justin Clancy, the shadow minister of New South Wales, '
               'Australia. SVU is determined to encourage employment-driven curriculum '
               'formation so that the entire learning process works as an enabling factor. Our '
               'avowed aim is to build definitive pathways to success and achievement. '
               'Multiple course strategies and correlated counselling methodologies have been '
               'adopted so that our students can turn themselves into future builders of the '
               'nation.']},
 {'name': 'Prof. (Dr.) Ranjan Chakrabarti',
  'role': 'Director , Research & Academic Development',
  'photo': 'img/our_team/ranjan-chakrabarti.jpg',
  'messages': ['I extend a warm welcome to you all to Swami Vivekananda University, located in '
               'the Barrackpore. As the Director ,Research & Academic Development of this '
               'esteemed institution, it is my privilege to address you and convey my vision '
               'for your educational journey. At Swami Vivekananda University, we are '
               'committed to providing a transformative learning experience that equips you '
               "with the knowledge, skills, and values necessary for success in today's "
               'dynamic world. Our dedicated faculty members, state-of-the-art facilities, and '
               'industry-oriented curriculum ensure that you receive a holistic education that '
               'prepares you to excel in your chosen field. As you embark on this enriching '
               'educational journey at Swami Vivekananda University, I urge you to make the '
               'most of every opportunity that comes your way. Embrace challenges, explore new '
               'avenues, and push your boundaries. Remember, education is not just about '
               'acquiring knowledge; it is about personal growth, character building, and '
               'lifelong learning. Once again, I extend my best wishes to you all. Together, '
               'let us embark on this transformative journey towards excellence.']},
 {'name': 'Prof.(Dr.) Malayendu Saha',
  'role': 'Director , School of Management',
  'photo': 'img/our_team/malayendu-saha.jpg',
  'messages': ['India, lately, has emerged as one of the significant economic and geopolitical '
               'powers amidst a challenging and competitive global scenario. Its action in the '
               'coming years, it is anticipated, could attribute in preparing the groundwork '
               'for the country to become the world’s third largest economy in the next five '
               'years and a developed nation by 2047, setting an example of an inclusive, '
               'sustainable economic growth, digital development and climate action. Keeping '
               'this backdrop in mind, it is very much needed to create an ideal '
               'learner-centric environment that attempts to ignite a spark in the minds of '
               'budding managers of the future, who are going to lead this change. It is '
               'perceived that the teaching-learning process with a curriculum that is a '
               'unique blend of strategic thinking and pragmatism would surely broaden the '
               'knowledge – horizon and enhance skills to cater to those aspirants. The '
               'School of Management of Swami Vivekananda University has been striving '
               'relentlessly to develop competent managerial human resources not only for '
               'Industry but the country at large, who are ready to take on the challenges of '
               'the ever-changing corporate environment. I am exhilarated to be part of Swami '
               'Vivekananda University fraternity and confident that the dedicated effort and '
               'unwavering support of our experienced Faculties would surely help the students '
               'to thrive in this knowledge-driven global economy and proceed towards a '
               'transformative journey of excellence together.']},
 {'name': 'Prof. Dr. Nirmal Kanti Chakrabarti',
  'role': 'Chief Advisor (School of Legal Studies)',
  'photo': 'img/our_team/nirmal-kanti-chakrabarti.jpg',
  'messages': ['In the twenty first century, as a result of globalization, legal instruction '
               'and discourse have taken more of an interdisciplinary format. The changes in '
               'Indian legal education began with the inception of the Advocates Act of 1961, '
               'which provided definitive rules for legal education that must be maintained by '
               'all institutions imparting the same. Currently, legal education in India, '
               'governed by the Bar Council of India, takes into account several innovative '
               'techniques such as seminars and conferences, moot courts, case studies, '
               'problem solving, and court visits, and is not limited to just a theoretical '
               'discussion of the law. It continues to discuss the importance of taking law as '
               'an interdisciplinary stream, in which where discourses on society, politics, '
               'economics, and science are crucial aspects. The current state of Indian legal '
               'education based on new and ground breaking technologies such as artificial '
               'intelligence and machine learning, and how those can be integrated into the '
               'justice system. We have to look into the 2020 National Education Policy and '
               'how that is likely to change the landscape of legal education in the country. '
               'The idea is that the legal discipline must grow and evolve to serve the needs '
               'of the society in question and to fulfil its pertinent objectives, instead of '
               'staying sedentary through the decades and centuries. The Indian judiciary has '
               'played a proactive role in striking down old and outdated laws which no longer '
               'serve the needs of the society. On the other hand, new legislations have been '
               'created, which are required to govern modern sectors and problems of the '
               'twenty first century.',
               'The objective of legal education is not to mould the students into a master of '
               'the written words of law, but they must also be able to analyse, criticize, '
               'and implement the same in the context of the problem at hand and the society '
               'at large. Only with such continuous criticism and discourse, rule of law in '
               'the society can be strengthened. The School of Legal Studies at Swamy '
               'Vivekananda University has been established to prepare the new generation of '
               'legal professional to achieve these objectives of legal education.']},
 {'name': 'Prof.(Dr.) Mita Banerjee',
  'role': 'Chief Academic Advisor (Department of Education)',
  'photo': 'img/our_team/mita-banerjee.jpg',
  'messages': ['Swami Vivekananda University aims to offer the best education to the students '
               'and holistically build humans who can lead the nation. At SVU, you will find a '
               'scholastic environment that encourages innovation and an urge to achieve '
               'excellence beyond ordinary. Highly qualified and committed faculties have '
               'enriched the University over the years. Experts in various fields are '
               'continuously developing new pedagogical techniques with the help of the '
               'state-of-the-art equipment. SVU cherish the motivation to nurture the goals '
               'and ambitions of the students and to provide them with the stage from where '
               'they are able to explore their full potential. Our curriculum and pedagogy '
               'includes new and interactive methods for fostering team and leadership spirit '
               'in the students, for enhancement of soft skills as well as vocational skills '
               'among the students. The University is currently in the process of establishing '
               'several national and international collaborations with leading institutions '
               'across the globe and create opportunities for higher study and internship '
               'programs.']},
 {'name': 'Prof.(Dr.) Swapan Kumar Datta',
  'role': 'Director, School of Agriculture',
  'photo': 'img/our_team/swapan-kumar-datta.jpg',
  'messages': ['Education is the most powerful weapon which you can use to change the world."',
               'Your power to choose the direction of your life allows you to reinvent '
               'yourself, to change your future, and to powerfully influence the rest. '
               'Leadership and learning are indispensable to each other. The only person who '
               'is educated is, the one who know how to learn and change. You are the "Change" '
               'to yourself and your future. You are welcome to Swami Vivekananda University. '
               'The institution provides you the space to ignite your imagination and inspire '
               'you to love learning.']},
 {'name': 'Prof.(Dr.) Anuradha Mukhopadhyay',
  'role': 'Director, School of Sciences',
  'photo': 'img/our_team/anuradha-mukhopadhyay.jpg',
  'messages': ['It is a great pleasure to serve as the Director of School of Science, Swami '
               'Vivekananda University (SVU).',
               'The university’s vision is to foster an environment that encourages students’ '
               'creativity, innovation, and brilliance. At SVU, we firmly believe in '
               'multidisciplinary research and development for the good of society and '
               'industry. We place a strong emphasis on cultivating all-around leadership '
               'abilities. We are pleased to state that the university is in a prime position '
               'to take advantage of the synergy between departments and faculties.',
               'The reputed scientific journal ‘Nature’ has listed Kolkata as topmost among '
               'Indian cities in its listing of 200 scientific cities in the world for this '
               'year. We in Kolkata involved in scientific research and teaching in SVU are '
               'not only proud of this achievement but must strive to maintain this standard '
               'if not to reach greater heights.',
               'We are sure that whatever we do will become noteworthy examples of '
               'accomplishments in the broader academic lexicon. We hope that our efforts in '
               'research and teaching-learning process will pay off in the form of citations, '
               'top-tier journal articles, technological advancements, and innovative academic '
               'work. Looking forward to a glorious future ahead.']},
 {'name': 'Prof. (Dr.) Pinak Pani Nath',
  'role': 'Registrar',
  'photo': 'img/our_team/pinak-pani-nath.png',
  'messages': ['Swami Vivekananda University has been gradually establishing itself as the '
               'most promising University among newly set up State Private Universities in the '
               "State and the nation. It's my proud privilege to be associated with this "
               'University and part of frameworking the same. I am hopeful that this '
               'University will transform itself as a lead University in its futuristic '
               'endeavour .']},
 {'name': 'Prof. (Dr)Sukumar Mukhopadhyay',
  'role': 'Controller of Examinations',
  'photo': 'img/our_team/sukumar-mukhopadhyay.jpg',
  'messages': ['We are very much proud to see the continued success and growth of our beloved '
               'institution, Swami Vivekanand University which has been playing a continuous '
               'significant role in shaping the specialization of the individual, making all '
               'the students ready for the social life, creating a learning environment within '
               'and outside the University campus where every student feels valued and '
               'empowered to reach full potential that fosters collaboration, creativity and '
               'intellectual curiosity.',
               'Our University emphasizes digital education and aims to increase the Gross '
               'Enrolment Ratio in higher education as well as to reform the Indian education '
               'system,following the five (5) pillars of National Education Policy (NEP), '
               'viz., access, equity, quality, affordability and accountability as well as '
               'providing ongoing professional development, incorporating modern teaching '
               'methods, focusing on student-centered learning approaches and qualitative '
               'examination system.',
               'Highest measures, viz., NAAC Accreditation status, accreditation to '
               'Engineering and Technology Courses, introduction of various scholarship and '
               'stipend and method to measure the performance of the individual members of the '
               'University have been taken by our University for quality improvement of higher '
               'education.',
               'We do hope that our University with a value system will continue to strive '
               'hard to achieve its mission of education apart from imparting purposeful '
               'education to students.']},
 {'name': 'Mr. Tanmoy Mazumder',
  'role': 'Deputy Registrar',
  'photo': 'img/our_team/tanmoy-mazumder.png',
  'messages': ['Welcome to the Swami Vivekananda University, Barrackpore, West Bengal, India. '
               'We are truly a pulsating university where ambitious students prepare '
               'themselves to be accountable leaders and enduring learners through rigorous '
               'engineering tutoring. With students in India looking for more '
               'inter-disciplinary programs and flexibility in course curriculum, SVU shifted '
               'the focus on to the manner the programs are offered, and the curriculum is '
               'designed. The programme and curriculum are designed in such a manner that the '
               'student has the freedom to decide the pathway to career progression. Our '
               'strengths are the top-class faculty members who take up scientific challenges '
               'through their research work and transfer their knowledge gained through '
               'research experience to the students. I am honoured to be part of a team of '
               'people who are committed, compassionate and team leaders, and keep SVU flag '
               'flying high.']},
 {'name': 'Mr. Abhishek Dhar',
  'role': 'Academic Coordinator , Assistant Professor , Department of Electrical Engineering',
  'photo': 'img/our_team/abhishek-dhar.png',
  'messages': ['Welcome to the Swami Vivekananda University, Barrackpore, West Bengal, India. '
               'We are truly a pulsating university where ambitious students prepare '
               'themselves to be accountable leaders and enduring learners through rigorous '
               'engineering tutoring. With students in India looking for more '
               'inter-disciplinary programs and flexibility in course curriculum, SVU shifted '
               'the focus on to the manner the programs are offered, and the curriculum is '
               'designed. The programme and curriculum are designed in such a manner that the '
               'student has the freedom to decide the pathway to career progression. Our '
               'strengths are the top-class faculty members who take up scientific challenges '
               'through their research work and transfer their knowledge gained through '
               'research experience to the students. I am honoured to be part of a team of '
               'people who are committed, compassionate and team leaders, and keep SVU flag '
               'flying high.']},
 {'name': 'Mr. Sourav Saha',
  'role': 'Deputy Controller of Examinations , Assistant Professor , Department of Computer '
          'Science & Engineering',
  'photo': 'img/our_team/sourav-saha.png',
  'messages': ['2020 was a remarkable year for all of us who are a part of the Swami '
               'Vivekananda University team. Starting a university is not something '
               'unthinkable, but starting a university amidst lockdown 2020 from scratch is, '
               'of course, touching and shows the tireless efforts of a team.',
               'Swami Vivekananda University has achieved excellence in its academic and '
               'research skills within a tiny span of time with the best infrastructure and '
               'faculties, and their constant support has helped students bloom. All this was '
               'possible because of the constant support, encouragement, and faith of our '
               'Chancellor, Dr. Nandan Gupta, and our very own Chief Operating Officer, Mr. '
               'Saurabh Adhikari.']},
 {'name': 'Mr. Saurabh Adhikari',
  'role': 'Chief Operating Officer',
  'photo': 'img/our_team/saurabh-adhikari.png',
  'messages': ['It was indeed a pleasure to find the website of our university in place. It '
               'reflects a picture of strengths, weaknesses, opportunities, and challenges '
               'faced from the very inception, in which we started with the dual calamities of '
               'the global pandemic and super-cyclone Amphan. However, with the help of all '
               'the stakeholders, the university emerges with its natural vibe, signifying '
               'growth and, at the same time, the lessons to be learned from our failures, if '
               'any. The pandemic, with its uncertain behaviour, has no doubt retarded the '
               'progress of almost all institutions, including ours. Under the guidance of our '
               'hon’ble Chancellor, we have faced the pandemic with clarity and planning, and '
               'many of our plans have been executed to our satisfaction. Still, we have miles '
               'to go, and our aim and goal are to see that our university emerges as one of '
               'the top-ranking universities in our country.']}]

# --------------------------------------------------------------------------
# Mentors and advisors, shown on /page/our-mentors/ using the same stacked
# panels as TEAM. Names, roles and photographs are real.
#
# 'messages' is intentionally empty. In the source build all 17 entries
# carried the SAME placeholder paragraph ("The Vice Chancellor's office is
# where a student's record lives..."), which is filler rather than anything
# these people said — and most of them hold posts at other universities, so
# the text did not even describe them. Publishing one invented quote 17
# times under named public figures would be worse than publishing none.
# Add a real message to any entry and that panel will render it.
MENTORS = [{'name': 'Prof. (Dr.) Suranjan Das',
  'role': 'Vice-Chancellor, Adamas University',
  'photo': 'img/our_mentors/suranjan-das.jpg',
  'messages': []},
 {'name': 'Prof. (Dr.) Dhrubajyoti Chattopadhyay',
  'role': 'Vice Chancellor, Sister Nivedita University Kolkata',
  'photo': 'img/our_mentors/dhrubajyoti-chattopadhyay.jpg',
  'messages': []},
 {'name': 'Prof. (Dr.) Shorosimohan Dan',
  'role': 'Former Vice Chancellor , The University of Burdwan',
  'photo': 'img/our_mentors/shorosimohan-dan.png',
  'messages': []},
 {'name': 'Prof. (Dr.)Deb Narayan Bandyopadhyay',
  'role': 'Founder Vice Chancellor,Bankura University',
  'photo': 'img/our_mentors/deb-narayan-bandyopadhyay.png',
  'messages': []},
 {'name': 'Prof. (Dr.) Ranjan Chakrabarti',
  'role': 'Former Vice-Chancellor Vidyasar University',
  'photo': 'img/our_mentors/ranjan-chakrabarti.jpg',
  'messages': []},
 {'name': 'Prof.(Dr.) Malayendu Saha',
  'role': 'Former Vice-Chancellor , Kalyani University',
  'photo': 'img/our_mentors/malayendu-saha.jpg',
  'messages': []},
 {'name': 'Prof.(Dr.) Mita Banerjee',
  'role': "Former Vice-Chancellor of The West Bengal University of Teachers' Training "
          'Education Planning and Administration',
  'photo': 'img/our_mentors/mita-banerjee.jpg',
  'messages': []},
 {'name': 'Prof.(Dr.) Swapan Kumar Datta',
  'role': 'Former Vice-Chancellor Visva-Bharati & Biswa Bangla Biswabidyalay',
  'photo': 'img/our_mentors/swapan-kumar-datta.jpg',
  'messages': []},
 {'name': 'Prof.(Dr.) Ashutosh Ghosh',
  'role': 'Former Vice-Chancellor Rani Rashmoni Green University , Former Pro Vice-Chancellor '
          ', (Academic Affairs) University of Calcutta',
  'photo': 'img/our_mentors/ashutosh-ghosh.jpg',
  'messages': []},
 {'name': 'Prof. (Dr.) Nemai Saha',
  'role': 'Former Vice-Chancellor , The University of Burdwan',
  'photo': 'img/our_mentors/nemai-saha.jpg',
  'messages': []},
 {'name': 'Dr. Baidyanath Chakrabarty',
  'role': 'Renowned Gynecologist and IVF Specialist',
  'photo': 'img/our_mentors/baidyanath-chakrabarty.jpg',
  'messages': []},
 {'name': 'Padmashri Bikash Sinha',
  'role': 'Former Director of the Saha Institute of Nuclear Physics and Variable Energy '
          'Cyclotron Centre and the chairman of the Board of Governors of the National '
          'Institute of Technology, Durgapur',
  'photo': 'img/our_mentors/bikash-sinha.jpg',
  'messages': []},
 {'name': 'Prof.(Dr.) Bashabi Fraser',
  'role': 'Professor Emerita of English and Creative Writing Director, Scottish Centre of '
          'Tagore Studies (ScoTs) School of Arts & Creative Industries Edinburgh Napier '
          'University Honorary Fellow, Centre for South Asian Studies, University of Edinburgh',
  'photo': 'img/our_mentors/bashabi-fraser.jpg',
  'messages': []},
 {'name': 'Prof. (Dr.) Neil Fraser',
  'role': 'Professor, School of Social and Political Studies, University of Edinburgh',
  'photo': 'img/our_mentors/neil-fraser.jpg',
  'messages': []},
 {'name': 'Prof.(Dr.) Arun Bandyopadhyay',
  'role': 'Director, Gujarat Biotechnology University, Gandhinagar. Former Director, '
          'CSIR-Indian Institute of Chemical Biology, Kolkata',
  'photo': 'img/our_mentors/arun-bandyopadhyay.jpg',
  'messages': []},
 {'name': 'Prof. (Dr.) Amlan Chakrabarti',
  'role': 'Head IT & Tech. Innovation Cell, Dept. of Higher Education, Govt. of West Bengal, '
          'Professor and Director, A.K. Choudhury School of IT, University of Calcutta',
  'photo': 'img/our_mentors/amlan-chakrabarti.png',
  'messages': []},
 {'name': 'Prof. (Dr.) Debprasad Chattopadhyay',
  'role': 'Founder Director & Scientist G at ICMR-National Institute of Traditional Medicine',
  'photo': 'img/our_mentors/debprasad-chattopadhyay.jpg',
  'messages': []}]

# --------------------------------------------------------------------------
# UGC Compliance Documents  —  /page/ugc-compliance/
#
# Each row becomes one card on the page, in the order written here. Give a row
# EITHER a file or a url, not both:
#
#   {'name': 'Public Self-Disclosure',
#    'file': 'documents/public-self-disclosure.pdf'},   # sits in static/
#
#   {'name': 'UGC Website',
#    'url': 'https://www.ugc.gov.in/'},                 # somewhere else
#
# A file path is resolved through {% static %}, so the PDF has to be in
# static/documents/ and collectstatic has to have run - a path with no manifest
# entry is a 500 in production, not a broken link.
#
# The list is empty on purpose. The page says so plainly rather than showing
# cards that lead nowhere; add rows and they appear, with no template to edit.
UGC_DOCUMENTS = []

# --------------------------------------------------------------------------
# Statutory approvals shown on /page/recognition-approvals/. Each card links a
# PDF in static/documents/.
#
# These four are the REAL certificates, uploaded under the names they came
# with - hence the mixed casing below. The names are load-bearing: they are
# what recognition_approvals.html asks {% static %} for. Replacing a document
# means overwriting the file of that name, or editing the name here to match
# the new one; the template never changes either way.
#
# That template uses a bare {% static %}, not the forgiving doc_url filter the
# notice board uses, so a name here with no manifest entry is a 500 on the
# page rather than one dead card. After adding or renaming a PDF, run:
#     python manage.py collectstatic --noinput
#
# Give an entry a 'url' key instead of 'file' to point a card at an external
# site.
# --------------------------------------------------------------------------
# List of Holidays  —  /page/list-of-holidays/
#
#   date      'YYYY-MM-DD'. The page sorts on this and works the weekday out
#             itself, so there is no day column to keep in step - change a
#             date and "Monday" changes with it. A date that has passed is
#             greyed on the page rather than removed.
#   occasion  the wording in the last column
#   note      optional, shown in smaller type under the occasion
#
# ONLY FIXED-DATE HOLIDAYS ARE LISTED HERE.
# Everything below falls on the same Gregorian date every year, so it can be
# published without checking. The festival holidays - Saraswati Puja, Doljatra,
# Good Friday, the two Eids, Durga Puja, Lakshmi Puja, Kali Puja, Bhai Phonta,
# Guru Nanak Jayanti - move with the lunar calendar and are NOT here, because
# guessing them on a page students plan around would be worse than leaving
# them out. Add them from the university's own holiday circular:
#
#     {'date': '2026-10-19', 'occasion': 'Durga Puja - Saptami'},
#
# Poila Boishakh and Rabindra Jayanti are listed at the dates West Bengal
# usually observes; confirm both against the circular, as each can shift a day.
HOLIDAYS = [
    {'date': '2026-01-01', 'occasion': "New Year's Day", 'note': ''},
    {'date': '2026-01-23', 'occasion': 'Netaji Subhas Chandra Bose Jayanti', 'note': ''},
    {'date': '2026-01-26', 'occasion': 'Republic Day', 'note': ''},
    {'date': '2026-04-14', 'occasion': 'Dr. B. R. Ambedkar Jayanti', 'note': ''},
    {'date': '2026-04-15', 'occasion': 'Poila Boishakh',
     'note': 'Bengali New Year'},
    {'date': '2026-05-01', 'occasion': 'May Day', 'note': ''},
    {'date': '2026-05-09', 'occasion': 'Rabindra Jayanti',
     'note': '25th Boishakh'},
    {'date': '2026-08-15', 'occasion': 'Independence Day', 'note': ''},
    {'date': '2026-10-02', 'occasion': 'Gandhi Jayanti', 'note': ''},
    {'date': '2026-12-25', 'occasion': 'Christmas Day', 'note': ''},
]

# --------------------------------------------------------------------------
# Academic Activities  —  /page/academic-activities/
#
# What the university runs alongside the syllabus. Each row is one card:
#
#   title        the heading on the card
#   description  a sentence or two under it
#   icon         a symbol from templates/includes/icons.html, without the
#                "i-" prefix. Anything there works: book, lab, research,
#                experts, industry, graduation, users, handshake, innovation.
#
# Add, remove or reorder rows and the grid follows - there is no template to
# edit. These describe standing activity rather than dated events; individual
# events belong in EVENTS, which drives /events/.
ACADEMIC_ACTIVITIES = [
    {'title': 'Seminars & Conferences',
     'icon': 'experts',
     'description': 'Departments host subject seminars and national conferences through the '
                    'year, with papers presented by faculty, research scholars and final-year '
                    'students alongside invited speakers.'},
    {'title': 'Workshops & Hands-On Training',
     'icon': 'lab',
     'description': 'Short practical workshops run beside the syllabus - laboratory technique, '
                    'software tools, instrumentation and design - so students practise skills '
                    'the timetable alone cannot cover.'},
    {'title': 'Faculty Development Programmes',
     'icon': 'book',
     'description': 'Teachers attend and run FDPs on curriculum design, assessment and new '
                    'developments in their disciplines, which is how the syllabus keeps pace '
                    'with the field.'},
    {'title': 'Guest Lectures',
     'icon': 'users',
     'description': 'Academics and practitioners from other institutions and from industry are '
                    'invited to teach a session, giving students a view of the subject from '
                    'outside their own department.'},
    {'title': 'Industrial Visits & Internships',
     'icon': 'industry',
     'description': 'Structured visits to working plants, laboratories and offices, and summer '
                    'internships arranged through the Training & Placement Cell, so classroom '
                    'work is tested against practice.'},
    {'title': 'Student Projects & Research',
     'icon': 'research',
     'description': 'Every programme carries project work, and undergraduates are attached to '
                    'departmental research groups and encouraged to publish, present and file '
                    'patents.'},
    {'title': 'Certification Courses',
     'icon': 'graduation',
     'description': 'Value-added certification courses run alongside the degree, letting a '
                    'student leave with credentials the syllabus does not itself award.'},
    {'title': 'Academic Collaborations',
     'icon': 'handshake',
     'description': 'Memoranda with other universities, research institutes and companies '
                    'support joint teaching, shared laboratories and collaborative research.'},
]


# --------------------------------------------------------------------------
# "Our Recruiters"  —  the second drifting band on the home page
#
# Same shape as AFFILIATIONS above and rendered by the same markup, so a row
# needs the same two keys:
#
#   caption  the company name, shown under the mark
#   logo     the mark, under static/img/industry/
#   url      OPTIONAL. Given one, the whole card links there in a new tab.
#
# The marks are shared with the Industry panel of /page/collaboration/, which
# is why they live in img/industry/ rather than a folder of their own — one
# copy of each file, used in both places.
RECRUITERS = [
    {'caption': 'Advanced Testing Equipments',
     'logo': 'img/industry/advanced.png', 'url': ''},
    {'caption': 'AE',
     'logo': 'img/industry/ae.png', 'url': ''},
    {'caption': 'AFCONS',
     'logo': 'img/industry/afc.png', 'url': ''},
    {'caption': 'Aimil',
     'logo': 'img/industry/aimil.png', 'url': ''},
    {'caption': 'AK Groups (Huion Official Partner)',
     'logo': 'img/industry/AK Groups (huion official partner).png', 'url': ''},
    {'caption': 'Ardent Computech Private Limited',
     'logo': 'img/industry/Ardent-computech-private-limited.jpg', 'url': ''},
    {'caption': 'ASTRAM Technologies (Pty) Ltd',
     'logo': 'img/industry/ASTRAM TECHNOLOGIES (PTY) LTD.webp', 'url': ''},
    {'caption': 'Autism Society West Bengal',
     'logo': 'img/industry/AUTISM SOCIETY WEST BENGAL.jpg', 'url': ''},
    {'caption': 'CANTek',
     'logo': 'img/industry/can.png', 'url': ''},
    {'caption': 'Chatto Andragogy Life Sciences',
     'logo': 'img/industry/andralogylifesciences.png', 'url': ''},
    {'caption': 'Circle of Hope Private Academy',
     'logo': 'img/industry/circleofhopeprivateacademycoha.png', 'url': ''},
    {'caption': 'Debgiri Agro Products',
     'logo': 'img/industry/debgiriagroproductspvtltd.png', 'url': ''},
    {'caption': 'Dhoot Transmission',
     'logo': 'img/industry/dhoottransmissionpvtltd.png', 'url': ''},
    {'caption': 'Digital Googly',
     'logo': 'img/industry/digital-googly-logo.jpg', 'url': ''},
    {'caption': 'Fluke',
     'logo': 'img/industry/fluke.png', 'url': ''},
    {'caption': 'Gammon India',
     'logo': 'img/industry/Gammon_India_Logo.svg.png', 'url': ''},
    {'caption': 'HCC',
     'logo': 'img/industry/hcc.svg', 'url': ''},
    {'caption': 'HPSM',
     'logo': 'img/industry/hpsm.png', 'url': ''},
    {'caption': 'IBM',
     'logo': 'img/industry/ibm.png', 'url': ''},
    {'caption': 'KYB Motorcycle Suspension India',
     'logo': 'img/industry/KYB MOTORCYCLE SUSPENSION INDIA PVT.LTD.jpeg', 'url': ''},
    {'caption': 'Larsen &amp; Toubro',
     'logo': 'img/industry/lt.png', 'url': ''},
    {'caption': 'Metravi',
     'logo': 'img/industry/metravi.png', 'url': ''},
    {'caption': 'Motherson',
     'logo': 'img/industry/Motherson.jpg', 'url': ''},
    {'caption': 'Nabajatak Child Development Centre',
     'logo': 'img/industry/Nabajatak Child development centre.png', 'url': ''},
    {'caption': 'Nature Technologies',
     'logo': 'img/industry/nature-technology-logo.jpg', 'url': ''},
    {'caption': 'OWASP',
     'logo': 'img/industry/owasp.jpg', 'url': ''},
    {'caption': 'Policy Research Centre',
     'logo': 'img/industry/policyresearchcentrebd.png', 'url': ''},
    {'caption': 'Premium Industrial Solutions',
     'logo': 'img/industry/pispl.png', 'url': ''},
    {'caption': 'Proceq',
     'logo': 'img/industry/proceq.png', 'url': ''},
    {'caption': 'Pushpanjali Eye Care',
     'logo': 'img/industry/PUSHPANJALI EYE CARE (A UNIT OF OPHTHATEK PVT LTD).png', 'url': ''},
    {'caption': 'Shrachi Group',
     'logo': 'img/industry/shrachigroup.png', 'url': ''},
    {'caption': 'SHRM',
     'logo': 'img/industry/shrm.jpg', 'url': ''},
    {'caption': 'Silver Screen Production House',
     'logo': 'img/industry/SILVER SCREEN Production house.png', 'url': ''},
    {'caption': 'Stonex',
     'logo': 'img/industry/stonex.png', 'url': ''},
    {'caption': 'Strucxial Projects Consultants',
     'logo': 'img/industry/strucxial projects consultants.png', 'url': ''},
    {'caption': 'Taparia',
     'logo': 'img/industry/taparia.png', 'url': ''},
    {'caption': 'TATA STRIVE',
     'logo': 'img/industry/tatastrive.png', 'url': ''},
    {'caption': 'TCS iON',
     'logo': 'img/industry/tcs-ion.jpg', 'url': ''},
    {'caption': 'Tutopia',
     'logo': 'img/industry/tutopiaprivatelimited.png', 'url': ''},
    {'caption': 'Unacademy',
     'logo': 'img/industry/unacademy-recog.jpg', 'url': ''},
    {'caption': 'Web Skitters',
     'logo': 'img/industry/webskitter.jpg', 'url': ''},
    {'caption': 'Webs Techno',
     'logo': 'img/industry/Webs-techno.jpg', 'url': ''},
]

# --------------------------------------------------------------------------
# Brochures  —  /page/brochure/
#
# One row per download, in the order they should appear. The grid reads ACROSS
# then down, two to a row on a desktop and one to a row on a phone, so keep
# "Main Brochure" first.
#
#   title  the wording on the row
#   file   the PDF, under static/documents/
#   url    use INSTEAD of 'file' to point a row at a document hosted elsewhere
#
# THE PDFs DO NOT HAVE TO EXIST YET
# Every row below is written before its file. The view resolves each path the
# forgiving way, so a row whose PDF has not been uploaded still appears - it
# just reads "Coming soon" instead of offering a download, rather than
# breaking the page. Drop the file into static/documents/ under the name
# written here, run
#     python manage.py collectstatic --noinput
# and that row turns into a download on its own, with nothing to edit.
BROCHURES = [
    {'title': 'Main Brochure',
     'file': 'documents/brochure-main.pdf'},
    {'title': 'School of Engineering',
     'file': 'img/brochure/Engg Brochure_compressed.pdf'},
    {'title': 'School of Management',
     'file': 'img/brochure/ManagementBrochure.pdf'},
    {'title': 'School of Computer Science',
     'file': 'documents/brochure-school-of-computer-science.pdf'},
    {'title': 'School of Humanities & Social Sciences',
     'file': 'img/brochure/Eng Journa Brochure_compressed.pdf'},
    {'title': 'School of Allied Health Services',
     'file': 'img/brochure/Allied Brochure_compressed.pdf'},
    {'title': 'School of Legal Studies',
     'file': 'documents/brochure-school-of-legal-studies.pdf'},
    {'title': 'School of Life Sciences',
     'file': 'documents/brochure-school-of-life-sciences.pdf'},
    {'title': 'School of Basic Sciences',
     'file': 'documents/brochure-school-of-basic-sciences.pdf'},
    {'title': 'School of Agriculture',
     'file': 'documents/brochure-school-of-agriculture.pdf'},
]

RECOGNITIONS = [
    {'name': 'Department Of Higher Education',
     'file': 'documents/kolkata.pdf'},
    {'name': 'Government Of West Bengal',
     'file': 'documents/ACT.pdf'},
    {'name': 'University Grants Commission',
     'file': 'documents/UGC.pdf'},
    {'name': 'Bar Council of India',
     'file': 'documents/Bar_Council_of_India.pdf'},
]

# --------------------------------------------------------------------------
# "Affiliation & Recognitions"  —  the drifting band on the home page
#
# Separate from RECOGNITIONS above, which is the four statutory bodies and
# their certificates. These are the awards, rankings and bodies the university
# is recognised by, and they carry a mark rather than a PDF.
#
#   caption  the line under the mark
#   logo     the mark, under static/img/AandR/
#   url      OPTIONAL. Given one, the whole card links there in a new tab.
#
# The marks are square and already carry their own whitespace, so the disc
# adds almost none of its own. A row whose file is missing shows its caption
# in the disc instead, so the band is never a row of blank circles.
AFFILIATIONS = [
    {'caption': "Institution's Innovation Council",
     'logo': 'img/AandR/01_institutions_innovation_council.png', 'url': ''},
    {'caption': 'Diamond Jubilee Celebration',
     'logo': 'img/AandR/02_diamond_jubilee_celebration.png', 'url': ''},
    {'caption': 'CEGR 2024 Education Excellence',
     'logo': 'img/AandR/03_cegr_2024_education_excellence.png', 'url': ''},
    {'caption': 'ABP Ananda Shiksha Samman 2024',
     'logo': 'img/AandR/04_abp_ananda_shiksha_samman_2024.png', 'url': ''},
    {'caption': 'News18 Bangla Education Eminence',
     'logo': 'img/AandR/05_news18_bangla_education_eminence.png', 'url': ''},
    {'caption': 'Academic Excellence Awards',
     'logo': 'img/AandR/06_academic_excellence_awards.png', 'url': ''},
    {'caption': 'R. Bharat Shiksha Samman',
     'logo': 'img/AandR/07_r_bharat_shiksha_samman.png', 'url': ''},
    # {'caption': 'Ministry of AYUSH',
    #  'logo': 'img/AandR/08_ministry_of_ayush.png', 'url': ''},
    # {'caption': 'Ranked by Outlook',
    #  'logo': 'img/AandR/09_outlook.png', 'url': ''},
    # {'caption': 'Ranked by The Week',
    #  'logo': 'img/AandR/10_the_week.png', 'url': ''},
    # {'caption': 'Internshala',
    #  'logo': 'img/AandR/11_internshala.png', 'url': ''},
    # {'caption': 'TimesSchool.com',
    #  'logo': 'img/AandR/12_times_school_com.png', 'url': ''},
]
