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
 'marquee_text': 'Beware of fake agents/consultants!! SVU does not take admission through any '
                 'agents/consultants. For any admission related query please refer to SVU '
                 'website only.',
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
 {'title': 'Programs',
  'href': '/academics/schools/',
  'is_external': False,
  'children': [{'title': 'SVU Schools', 'href': '/academics/schools/', 'is_external': False},
               {'title': 'Departments',
                'href': '/academics/departments/',
                'is_external': False},
               {'title': 'Schools & Courses',
                'href': '/academics/courses/',
                'is_external': False},]},
               
              
 {'title': 'Academic',
  'href': '/admission/',
  'is_external': False,
  'children': [{'title': 'Academics Overview', 'href': '#', 'is_external': False},
               {'title': 'List of Holidays', 'href': '#', 'is_external': False},
               {'title': 'Library', 'href': 'https://svu.knimbus.com/portal/v2/default/home', 'is_external': True},
               {'title': 'Academic Calendar','href': '/page/academic-calendar/', 'is_external': False},
                ]},
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
               {'title': 'Annual Report', 'href': '/page/annual-report/', 'is_external': False},
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
               {'title': 'Newsletter', 'href': '/page/newsletter/', 'is_external': False},

               {'title': 'Publication', 'href': '/page/publication/', 'is_external': False},
               {'title': 'Project', 'href': '/page/project/', 'is_external': False},
               {'title': 'Regulations', 'href': '/page/regulations/', 'is_external': False},
               {'title': 'Student Handbook', 'href': '/page/student-handbook/', 'is_external': False},
               {'title': 'Social Outreach Activities', 'href': '/page/social-outreach-activities/', 'is_external': False},
               {'title': 'Testing Facilities', 'href': '/page/testing-facilities/', 'is_external': False},
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
               {'title': 'Industry Collaboration',
                'href': '/academics/industry-partners/',
                'is_external': False}]},

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
            {'title': 'NPTEL Courses', 'url': 'https://nptel.ac.in/', 'is_external': True},
            {'title': 'SWAYAM', 'url': 'https://swayam.gov.in/', 'is_external': True},
            ]},

 {'title': 'Our Links',
  'links': [
      
            
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
            {'title': 'Library', 'url': 'https://svu.knimbus.com/portal/v2/default/home', 'is_external': True},
            ]},

 {'title': 'Quick Links',
  'links': [
            {'title': 'Student Services', 'url': '/page/student-services/', 'is_external': False},
            {'title': 'Placements', 'url': '/page/placements/', 'is_external': False},
            {'title': 'Research & Innovation', 'url': '/page/research-innovation/', 'is_external': False},
            {'title': 'Blogs', 'url': '/page/blogs/', 'is_external': False},
            {'title': 'Contact Us', 'url': '/contact/', 'is_external': False}]},
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
OFFERINGS = [{'title': 'Curriculum',
  'description': 'SVU is committed to provide an effective and dynamic curriculum with a '
                 'distinctive mission to transform lives through education.',
  'icon': 'curriculum'},
 {'title': 'Tech Classroom',
  'description': 'The digital whiteboards make learning methods to be the most interactive. '
                 'Our faculty provides academic training through smart classrooms.',
  'icon': 'classroom'},
 {'title': 'Experts',
  'description': "SVU's course features expert faculty to impart quality training to the "
                 'students.',
  'icon': 'experts'},
 {'title': 'Digital Library',
  'description': 'We are pleased to offer an online storehouse of knowledge to maintain '
                 'text-books, notes, journals, e-thesis, maps, rare books, and other important '
                 'documents with the advent of digital technology!',
  'icon': 'library'}]

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
CENTRES = [
    {'title': '',
  'description': '',
  'image': 'img/slides/coe.png',            # no photograph yet - the icon shows
  'alt_text': 'Centre for Innovation & Entrepreneurship',
  'icon': 'innovation',
  'url': ''},

 {'title': '',
  'description': '',
  'image': 'img/slides/coex.png',            # no photograph yet - the icon shows
  'alt_text': 'Industry Collaboration',
  'icon': 'industry',
  'url': ''},


 {'title': '',
  'description': '',
  'image': 'img/slides/ic.png',            # no photograph yet - the icon shows
  'alt_text': 'Centre of Excellence',
  'icon': 'excellence',
  'url': ''},


 {'title': '',
  'description': "",     
  'image': 'img/slides/ws.png',            # no photograph yet - the icon shows
  'alt_text': 'Swami Vivekananda Centre for Women Studies',
  'icon': 'women',
  'url': ''}
  ]

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

DEPARTMENTS = [
 # --- School of Engineering ---
 {'slug': 'department-of-computer-science-engineering',
  'name': 'Department Of Computer Science & Engineering',
  'school': 'school-of-engineering',
  'short_description': 'Diploma, B.Tech, M.Tech and Ph.D programmes in computing, with '
                       'laboratories for AI, data science, networking and software engineering.'},




 {'slug': 'department-of-electronics-communication-engineering',
  'name': 'Department Electronics & Communication Engineering',
  'school': 'school-of-engineering',
  'short_description': 'Analog and digital electronics, embedded systems, VLSI and '
                       'communication engineering.'},


 {'slug': 'department-of-electrical-engineering',
  'name': 'Department Of Electrical Engineering',
  'school': 'school-of-engineering',
  'short_description': 'Analog and digital electronics, embedded systems, VLSI and '
                       'communication engineering.'},



 {'slug': 'department-of-civil-engineering',
  'name': 'Department Of Civil Engineering',
  'school': 'school-of-engineering',
  'short_description': 'Structural, geotechnical, transportation and environmental engineering '
                       'with a full survey and materials testing laboratory.'},





  {
    'slug': 'department-of-mechanical-engineering',
    'name': 'Department Of Mechanical Engineering',
    'school': 'school-of-engineering',
    'short_description': 'Advanced mechanical engineering education covering design, thermal, manufacturing and industrial systems with hands-on CAD/CAM, '
    'workshop and fluid mechanics laboratory training.',
},

 # --- School of Management & Commerce ---
 {'slug': 'department-of-management-studies',
  'name': 'Management Studies',
  'school': 'school-of-management',
  'short_description': 'BBA and MBA programmes covering marketing, finance, human resources '
                       'and operations, taught through cases and live projects.'},


 # --- School of Life Sciences & Biotechnology ---
 {'slug': 'biotechnology',
  'name': 'Biotechnology',
  'school': 'school-of-life-sciences',
  'short_description': 'Molecular biology, genetic engineering and bioprocess technology at '
                       'undergraduate and postgraduate level.'},
 {'slug': 'microbiology',
  'name': 'Microbiology',
  'school': 'school-of-life-sciences',
  'short_description': 'Medical, industrial and food microbiology with a dedicated culture '
                       'and fermentation laboratory.'},

 # --- School of Nursing & Allied Health Sciences ---
 {'slug': 'nursing',
  'name': 'Nursing',
  'school': 'school-of-allied-health-services',
  'short_description': 'B.Sc and Post Basic B.Sc Nursing with simulation laboratories and '
                       'supervised clinical postings in associated hospitals.'},
 {'slug': 'physiotherapy',
  'name': 'Physiotherapy',
  'school': 'school-of-allied-health-services',
  'short_description': 'Musculoskeletal, neurological and sports physiotherapy, including a '
                       'compulsory rotating internship.'},

 # --- School of Humanities & Social Sciences ---
 {'slug': 'journalism-mass-communication',
  'name': 'Journalism & Mass Communication',
  'school': 'school-of-humanities-social-science',
  'short_description': 'Print, broadcast and digital media practice, with an in-house studio '
                       'and editing suite.'},
 {'slug': 'psychology',
  'name': 'Psychology',
  'school': 'school-of-humanities-social-science',
  'short_description': 'Cognitive, clinical and counselling psychology supported by a '
                       'psychological testing laboratory.'},
 {'slug': 'sociology',
  'name': 'Sociology',
  'school': 'school-of-humanities-social-science',
  'short_description': 'Social theory, research methods and field-based study of rural and '
                       'urban communities in Bengal.'},

 # --- School of Basic & Applied Sciences ---
 {'slug': 'computer-applications',
  'name': 'Computer Applications',
  'school': 'school-of-basic-sciences',
  'short_description': 'BCA and MCA programmes covering programming, databases, web '
                       'technology and application development.'},
 {'slug': 'mathematics',
  'name': 'Mathematics',
  'school': 'school-of-basic-sciences',
  'short_description': 'Pure and applied mathematics, numerical methods and the foundation '
                       'courses that run across every engineering programme.'},

 # --- School of Pharmaceutical Sciences ---
 # Commented out together with its school in SCHOOLS above.  Uncomment this
 # department and the two D.Pharm/B.Pharm courses in COURSES when the school
 # comes back, otherwise they have no school to hang from.
 # {'slug': 'pharmacy',
 #  'name': 'Pharmacy',
 #  'school': 'school-of-pharmacy',
 #  'short_description': 'B.Pharm and D.Pharm programmes with PCI-aligned pharmaceutics, '
 #                       'pharmacology and pharmaceutical chemistry laboratories.'},

 # --- School of Legal Studies ---
 {'slug': 'law',
  'name': 'Law',
  'school': 'school-of-Legal-Studies',
  'short_description': 'Integrated and postgraduate law programmes with moot court training, '
                       'a legal aid clinic and court internships.'}]

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
# "{department}" is swapped for the department name when the page renders.
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
]

# --------------------------------------------------------------------------
COURSES = [


 {
    'slug': 'diploma-in-computer-science-technology',
    'name': 'Diploma in Computer Science & Technology',
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
    'school': 'school-of-engineering',
    'department': 'department-of-computer-science-engineering',
    'program': 'phd',
    'duration': '5 Years',
    'total_seats': 20,
    'is_featured': True,
    'eligibility': 'Master’s degree in Computer Science & Engineering, Information Technology, Computer Applications, or a related discipline from a recognised university with a minimum of 55% aggregate marks. Candidates may be required to qualify through the university admission process, including an entrance examination and/or interview.',
    'description': 'The Ph.D. programme in Computer Science & Engineering focuses on advanced research, innovation and specialised study in emerging areas of computing. Scholars undertake research under expert faculty guidance, complete required coursework and develop an original research thesis contributing to the field.'
},





 {'slug': 'b-tech-in-electronics-communication-engineering',
  'name': 'B.Tech in Electronics & Communication Engineering',
  'school': 'school-of-engineering',
  'department': 'electronics-communication-engineering',
  'program': 'under-graduate',
  'duration': '4 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed 10+2 with Physics, Chemistry and Mathematics as main subjects and a '
                 'minimum of 50% aggregate from a recognised board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},


 {'slug': 'b-tech-in-civil-engineering',
  'name': 'B.Tech in Civil Engineering',
  'school': 'school-of-engineering',
  'department': 'civil-engineering',
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
  'school': 'school-of-engineering',
  'department': 'mechanical-engineering',
  'program': 'under-graduate',
  'duration': '4 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 with Physics, Chemistry and Mathematics as main subjects and a '
                 'minimum of 50% aggregate from a recognised board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},



                 
 {'slug': 'm-tech-in-computer-science-engineering',
  'name': 'M.Tech in Computer Science & Engineering',
  'school': 'school-of-engineering',
  'department': 'computer-science-engineering',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 18,
  'is_featured': True,
  'eligibility': 'B.Tech / B.E. in Computer Science, IT, Electronics & Communication or '
                 'Electronics & Instrumentation Engineering with a minimum of 50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'diploma-in-computer-science-technology',
  'name': 'Diploma in Computer Science & Technology',
  'school': 'school-of-engineering',
  'department': 'computer-science-engineering',
  'program': 'diploma',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed the secondary or equivalent examination with a minimum of 35% from a '
                 'recognised board, including English and Physical Science / Mathematics.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'ph-d-in-computer-science-engineering',
  'name': 'Ph.D in Computer Science & Engineering',
  'school': 'school-of-engineering',
  'department': 'computer-science-engineering',
  'program': 'phd',
  'duration': '3-5 Years',
  'total_seats': 10,
  'is_featured': False,
  'eligibility': "Master's degree or equivalent from a recognised university with a minimum of "
                 '55% marks, followed by the university research entrance test and interview.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'bachelor-of-business-administration-bba',
  'name': 'Bachelor of Business Administration (BBA)',
  'school': 'school-of-management',
  'department': 'management-studies',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': True,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'b-com-honours',
  'name': 'B.Com (Honours)',
  'school': 'school-of-management',
  'department': 'commerce',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'master-of-business-administration-mba',
  'name': 'Master of Business Administration (MBA)',
  'school': 'school-of-management',
  'department': 'management-studies',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': "Bachelor's degree in any discipline with a minimum of 50% aggregate. Valid "
                 'MAT / CAT / CMAT score is preferred.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'b-sc-in-biotechnology',
  'name': 'B.Sc in Biotechnology',
  'school': 'school-of-life-sciences',
  'department': 'biotechnology',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed 10+2 in the science stream with Biology / Biotechnology and a minimum '
                 'of 45% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'b-sc-in-microbiology',
  'name': 'B.Sc in Microbiology',
  'school': 'school-of-life-sciences',
  'department': 'microbiology',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in the science stream with Biology and a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'm-sc-in-biotechnology',
  'name': 'M.Sc in Biotechnology',
  'school': 'school-of-life-sciences',
  'department': 'biotechnology',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 30,
  'is_featured': False,
  'eligibility': 'B.Sc in Biotechnology, Microbiology, Zoology, Botany or an allied '
                 'life-science discipline with a minimum of 50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'b-sc-nursing',
  'name': 'B.Sc Nursing',
  'school': 'school-of-allied-health-services',
  'department': 'nursing',
  'program': 'under-graduate',
  'duration': '4 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed 10+2 with Physics, Chemistry, Biology and English, securing a minimum '
                 'of 45% aggregate. Candidate must be at least 17 years of age.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'post-basic-b-sc-nursing',
  'name': 'Post Basic B.Sc Nursing',
  'school': 'school-of-allied-health-services',
  'department': 'nursing',
  'program': 'under-graduate',
  'duration': '2 Years',
  'total_seats': 30,
  'is_featured': False,
  'eligibility': 'GNM qualified with registration as a Registered Nurse and Registered Midwife '
                 'with the state nursing council.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'bachelor-of-physiotherapy-bpt',
  'name': 'Bachelor of Physiotherapy (BPT)',
  'school': 'school-of-allied-health-services',
  'department': 'physiotherapy',
  'program': 'under-graduate',
  'duration': '4.5 Years',
  'total_seats': 40,
  'is_featured': False,
  'eligibility': 'Passed 10+2 with Physics, Chemistry and Biology, securing a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'ba-honours-in-journalism-mass-communication',
  'name': 'BA (Honours) in Journalism & Mass Communication',
  'school': 'school-of-humanities-social-science',
  'department': 'journalism-mass-communication',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'ba-honours-in-psychology',
  'name': 'BA (Honours) in Psychology',
  'school': 'school-of-humanities-social-science',
  'department': 'psychology',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'ba-honours-in-sociology',
  'name': 'BA (Honours) in Sociology',
  'school': 'school-of-humanities-social-science',
  'department': 'sociology',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'ma-in-journalism-mass-communication',
  'name': 'MA in Journalism & Mass Communication',
  'school': 'school-of-humanities-social-science',
  'department': 'journalism-mass-communication',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 30,
  'is_featured': False,
  'eligibility': "Bachelor's degree in any discipline with a minimum of 50% aggregate.",
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'bachelor-of-computer-applications-bca',
  'name': 'Bachelor of Computer Applications (BCA)',
  'school': 'school-of-basic-sciences',
  'department': 'computer-applications',
  'program': 'under-graduate',
  'duration': '3 Years',
  'total_seats': 120,
  'is_featured': True,
  'eligibility': 'Passed 10+2 with Mathematics or Computer Science and a minimum of 45% '
                 'aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'master-of-computer-applications-mca',
  'name': 'Master of Computer Applications (MCA)',
  'school': 'school-of-basic-sciences',
  'department': 'computer-applications',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 60,
  'is_featured': False,
  'eligibility': 'BCA / B.Sc in Computer Science / IT or a bachelor degree with Mathematics at '
                 '10+2 or graduation level, with a minimum of 50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'm-sc-in-mathematics',
  'name': 'M.Sc in Mathematics',
  'school': 'school-of-basic-sciences',
  'department': 'mathematics',
  'program': 'post-graduate',
  'duration': '2 Years',
  'total_seats': 30,
  'is_featured': False,
  'eligibility': 'B.Sc with Mathematics as an honours or major subject, securing a minimum of '
                 '50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 # Pharmacy courses, parked with their school and department — uncomment all
 # three together when the School of Pharmaceutical Sciences returns.
 # {'slug': 'bachelor-of-pharmacy-b-pharm',
 #  'name': 'Bachelor of Pharmacy (B.Pharm)',
 #  'school': 'school-of-pharmacy',
 #  'department': 'pharmacy',
 #  'program': 'under-graduate',
 #  'duration': '4 Years',
 #  'total_seats': 100,
 #  'is_featured': True,
 #  'eligibility': 'Passed 10+2 with Physics, Chemistry and Biology / Mathematics, securing a '
 #                 'minimum of 45% aggregate.',
 #  'description': 'The programme blends classroom instruction, laboratory or field practice and '
 #                 'continuous internal assessment. Students are mentored throughout the course '
 #                 'and prepared for placement through the training and placement cell.'},
 # {'slug': 'diploma-in-pharmacy-d-pharm',
 #  'name': 'Diploma in Pharmacy (D.Pharm)',
 #  'school': 'school-of-pharmacy',
 #  'department': 'pharmacy',
 #  'program': 'diploma',
 #  'duration': '2 Years',
 #  'total_seats': 60,
 #  'is_featured': False,
 #  'eligibility': 'Passed 10+2 with Physics, Chemistry and Biology / Mathematics from a '
 #                 'recognised board.',
 #  'description': 'The programme blends classroom instruction, laboratory or field practice and '
 #                 'continuous internal assessment. Students are mentored throughout the course '
 #                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'ba-ll-b-honours',
  'name': 'BA LL.B (Honours)',
  'school': 'school-of-Legal-Studies',
  'department': 'law',
  'program': 'under-graduate',
  'duration': '5 Years',
  'total_seats': 60,
  'is_featured': True,
  'eligibility': 'Passed 10+2 in any stream with a minimum of 45% aggregate from a recognised '
                 'board.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'},
 {'slug': 'll-m',
  'name': 'LL.M',
  'school': 'school-of-Legal-Studies',
  'department': 'law',
  'program': 'post-graduate',
  'duration': '1 Year',
  'total_seats': 30,
  'is_featured': False,
  'eligibility': 'LL.B or an equivalent law degree with a minimum of 50% aggregate.',
  'description': 'The programme blends classroom instruction, laboratory or field practice and '
                 'continuous internal assessment. Students are mentored throughout the course '
                 'and prepared for placement through the training and placement cell.'}]

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
# The home slider takes the FIRST SIX of these and shows two at a time,
# sliding one along every few seconds. Reorder the rows to change which six
# appear; the slice is in views.home, not here.
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
# TODO: the alt text below is generic because the images could not be opened
# when this was written. Replace each line with what its picture actually says.
APPRECIATIONS = [
 {'image': 'img/achivements/482247234_972659861637453_1522331182250338419_n.jpg.jpeg',
  'alt_text': 'An appreciation received by Swami Vivekananda University'},
 {'image': 'img/achivements/481233106_972665624970210_8860091325710493319_n.jpg.jpeg',
  'alt_text': 'An appreciation received by Swami Vivekananda University'},
 {'image': 'img/achivements/540903586_1105990141637757_7221139477378257898_n.jpg.jpeg',
  'alt_text': 'An appreciation received by Swami Vivekananda University'},
 {'image': 'img/achivements/NPTEL_1.jpeg',
  'alt_text': 'An NPTEL award presented to a member of the faculty'},
 {'image': 'img/achivements/MPTEL_2.jpeg',
  'alt_text': 'An NPTEL award presented to a member of the faculty'},
 {'image': 'img/achivements/rbangla.jpeg',
  'alt_text': 'An appreciation received by Swami Vivekananda University'},
 {'image': 'img/achivements/MPTEL_3.jpeg',
  'alt_text': 'An NPTEL award presented to a member of the faculty'},
 {'image': 'img/achivements/MPTEL_4.jpeg',
  'alt_text': 'An NPTEL award presented to a member of the faculty'},
 {'image': 'img/achivements/481979442_972665414970231_8854528053355663625_n.jpg.jpeg',
  'alt_text': 'An appreciation received by Swami Vivekananda University'},
 {'image': 'img/achivements/536270821_1105990098304428_367322835841659546_n.jpg.jpeg',
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
  'document': 'documents/bar-council-of-india.pdf',
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
  'messages': ["The Vice Chancellor's office sets the academic direction of the university — curriculum design, research priorities, faculty development and accreditation. Students meet that work in the form of syllabi that keep pace with the field, laboratories that are actually used, and teachers who are still learning themselves."]},
 {'name': 'Prof. (Dr.) Dhrubajyoti Chattopadhyay',
  'role': 'Vice Chancellor, Sister Nivedita University Kolkata',
  'photo': 'img/our_mentors/dhrubajyoti-chattopadhyay.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof. (Dr.) Shorosimohan Dan',
  'role': 'Former Vice Chancellor , The University of Burdwan',
  'photo': 'img/our_mentors/shorosimohan-dan.png',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof. (Dr.)Deb Narayan Bandyopadhyay',
  'role': 'Founder Vice Chancellor,Bankura University',
  'photo': 'img/our_mentors/deb-narayan-bandyopadhyay.png',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof. (Dr.) Ranjan Chakrabarti',
  'role': 'Former Vice-Chancellor Vidyasar University',
  'photo': 'img/our_mentors/ranjan-chakrabarti.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof.(Dr.) Malayendu Saha',
  'role': 'Former Vice-Chancellor , Kalyani University',
  'photo': 'img/our_mentors/malayendu-saha.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof.(Dr.) Mita Banerjee',
  'role': "Former Vice-Chancellor of The West Bengal University of Teachers' Training "
          'Education Planning and Administration',
  'photo': 'img/our_mentors/mita-banerjee.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof.(Dr.) Swapan Kumar Datta',
  'role': 'Former Vice-Chancellor Visva-Bharati & Biswa Bangla Biswabidyalay',
  'photo': 'img/our_mentors/swapan-kumar-datta.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof.(Dr.) Ashutosh Ghosh',
  'role': 'Former Vice-Chancellor Rani Rashmoni Green University , Former Pro Vice-Chancellor '
          ', (Academic Affairs) University of Calcutta',
  'photo': 'img/our_mentors/ashutosh-ghosh.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof. (Dr.) Nemai Saha',
  'role': 'Former Vice-Chancellor , The University of Burdwan',
  'photo': 'img/our_mentors/nemai-saha.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Dr. Baidyanath Chakrabarty',
  'role': 'Renowned Gynecologist and IVF Specialist',
  'photo': 'img/our_mentors/baidyanath-chakrabarty.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Padmashri Bikash Sinha',
  'role': 'Former Director of the Saha Institute of Nuclear Physics and Variable Energy '
          'Cyclotron Centre and the chairman of the Board of Governors of the National '
          'Institute of Technology, Durgapur',
  'photo': 'img/our_mentors/bikash-sinha.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof.(Dr.) Bashabi Fraser',
  'role': 'Professor Emerita of English and Creative Writing Director, Scottish Centre of '
          'Tagore Studies (ScoTs) School of Arts & Creative Industries Edinburgh Napier '
          'University Honorary Fellow, Centre for South Asian Studies, University of Edinburgh',
  'photo': 'img/our_mentors/bashabi-fraser.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof. (Dr.) Neil Fraser',
  'role': 'Professor, School of Social and Political Studies, University of Edinburgh',
  'photo': 'img/our_mentors/neil-fraser.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof.(Dr.) Arun Bandyopadhyay',
  'role': 'Director, Gujarat Biotechnology University, Gandhinagar. Former Director, '
          'CSIR-Indian Institute of Chemical Biology, Kolkata',
  'photo': 'img/our_mentors/arun-bandyopadhyay.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof. (Dr.) Amlan Chakrabarti',
  'role': 'Head IT & Tech. Innovation Cell, Dept. of Higher Education, Govt. of West Bengal, '
          'Professor and Director, A.K. Choudhury School of IT, University of Calcutta',
  'photo': 'img/our_mentors/amlan-chakrabarti.png',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]},
 {'name': 'Prof. (Dr.) Debprasad Chattopadhyay',
  'role': 'Founder Director & Scientist G at ICMR-National Institute of Traditional Medicine',
  'photo': 'img/our_mentors/debprasad-chattopadhyay.jpg',
  'messages': ["The Vice Chancellor's office is where a student's record lives: admission, enrolment, examinations, results and the certificates that follow them into their career. Its work is to make sure the administrative side of a degree is never the thing that slows a student down."]}]

# --------------------------------------------------------------------------
# Statutory approvals shown on /page/recognition-approvals/. Each card links a
# PDF in static/documents/.
#
# Every file there is a PLACEHOLDER - open one and it says so in the document
# itself. To publish a real certificate, overwrite the file of the same name;
# nothing here changes. Give an entry a 'url' key instead of 'file' to point a
# card at an external site.
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

RECOGNITIONS = [
    {'name': 'Department Of Higher Education',
     'file': 'documents/department-of-higher-education.pdf'},
    {'name': 'Government Of West Bengal',
     'file': 'documents/government-of-west-bengal.pdf'},
    {'name': 'University Grants Commission',
     'file': 'documents/university-grants-commission.pdf'},
    {'name': 'Bar Council of India',
     'file': 'documents/bar-council-of-india.pdf'},
]
