# Swami Vivekananda University — front end

A Django front end for Swami Vivekananda University, laid out on the Sister
Nivedita University template (gold utility bar, yellow navigation, full-height
hero video, notice board / welcome / enquiry band, school and event carousels,
chancellor block, dark footer).

**This build is front end only.** There is no database, no models and no admin
panel. Every page is rendered from plain Python data through views, which is what
keeps the content easy to change while it is still being decided.

---

## Running it

```bash
pip install -r requirements.txt
python manage.py runserver
```

Then open <http://127.0.0.1:8000/>. Nothing else is needed — no `migrate`, no
`createsuperuser`, no database file.

---

## How the content flows

```
website/data.py   ->   website/views.py   ->   templates/
   the content         picks + decorates        the markup
```

* **`website/data.py`** — every piece of text and every image path on the site:
  site identity, navigation, hero slides, notices, schools, courses, events,
  facilities, testimonials, FAQs and editorial pages.
* **`website/views.py`** — one function per page. It reads from `data.py`, adds
  the things templates should not compute (resolved URLs, real `date` objects,
  pagination, filtering, search) and renders a template.
* **`website/context_processors.py`** — the header, navigation and footer, which
  every page needs.

To change wording or swap an image, edit `data.py`. To change what a page shows,
edit `views.py`. To change the layout, edit the template.

### Adding a page

1. Add the content to `data.py`.
2. Add a view in `views.py`.
3. Add the route in `website/urls.py`.
4. Add the template under `templates/pages/`.

Editorial pages need only step 1: add a key to `PAGES` and it is live at
`/page/<slug>/`. Any menu link whose page has not been written yet still resolves
— it renders a "being prepared" panel instead of a 404, so no menu item is ever
a dead end.

**About Us** is the exception. It is a bespoke page rather than an editorial
one, so it has its own template, stylesheet and view:

* `templates/pages/about.html` — banner, split intro and the four-tab panel
* `static/css/about.css` — loaded only by that page, on top of `main.css`
* `views.about`, routed at `/page/about-svu/` *before* the generic `page/<slug>/`
  rule, so the existing menu links keep working unchanged

It is deliberately **not** in `PAGES`; the search view indexes it by hand
instead. Layout and copy were ported from the earlier `cu_clone` build, with the
header, footer and Bootstrap dependency dropped — tab switching is plain JS
(`initAboutTabs` in `main.js`), and the icons come from the existing SVG sprite.

The intro, the two affiliation dates and the five awards are the university's own
copy. The mission, core-values and salient-features panes are written in the
university's voice and should be replaced with the official statements — that
caveat sits in a comment beside them.

**Our Team** (`/page/our-team/`) and **Our Mentors** (`/page/our-mentors/`) are
built the same way and share their markup:

* `templates/includes/people_stack.html` — the panels themselves, used by both
  pages: a dark intro band, then one panel per person, each sticky at `top:0`
  so the next rides up and covers it
* `templates/pages/our_team.html` / `our_mentors.html` — thin wrappers that
  link the stylesheet and include the stack
* `static/css/team.css` — ported from the earlier build's `mentors.css`, keeping
  only the panels (the video hero and Swiper carousel in that file belong to a
  different page and are not reproduced)
* `views.our_team` / `views.our_mentors`, both routed before the generic rule

Each view passes `people`, `stack_title` and `stack_lead`, so restyling a panel
in the shared include updates both pages at once.

**Recognition & Approvals** (`/page/recognition-approvals/`) follows the same
shape: `templates/pages/recognition_approvals.html`, `static/css/recognition.css`
and `views.recognition_approvals`, with the four bodies listed in
`data.RECOGNITIONS`.

Each card links a PDF in `static/documents/`. **Every one of those files is a
placeholder** — open it and the document says so. To publish a real
certificate, overwrite the file of the same name; neither the template nor
`data.py` changes. The page says so on the record too, rather than presenting
placeholders as certificates. Give an entry a `url` key instead of `file` to
point a card at an external site.

The photo banner and the section heading with its rule are shared by About Us
and Recognition & Approvals, so they live in `static/css/page-head.css`
(`.page-banner`, `.page-heading`, `.page-rule`) rather than in either page's
own stylesheet. Both pages load it before their own CSS.

Mentors currently render photo, name and role with no message. That is
deliberate and the reason is written above `MENTORS` in `data.py`: the source
build repeated one placeholder paragraph across all 17 entries, and most of
those people hold posts at other universities, so the text did not describe
them either. Add a real message to any entry and that panel renders it.

Unlike About Us, the content is **data-driven**: 20 near-identical panels would
be 20 copies of the same markup, so the people live in `data.TEAM` and the
template loops. Adding, removing or reordering someone is a `data.py` edit —
the panels alternate sides via `:nth-of-type` and the `/ NN` counter reads the
list length, so both follow automatically.

Photos are in `static/img/our_team/`, renamed to clean slugs
(`nandan-gupta.png` rather than `17363489181. Chancellor.png`) — spaces and
double extensions in a static path are a liability once `collectstatic` and a
manifest are involved.

Two constraints in `team.css` are load-bearing and worth reading the comments
before changing: the `.team-speech` measure is 96ch (not the ~60ch a reading
measure would want) and sticky is dropped below 992px **and** under 700px of
viewport height. Both exist because a sticky panel taller than the screen pins
at `top:0` with its bottom below the fold, leaving the end of the message
unreachable. If a new message overflows, cut the copy rather than the type.

When editing either template, note that Django's `{# … #}` comment covers a
**single line only**. A two-line hash comment renders onto the page; use
`{% comment %}…{% endcomment %}` for anything longer.

---

## Layout

```
config/                 settings, root urls, wsgi/asgi
website/
  data.py               all site content
  views.py              one function per page
  urls.py               routes
  forms.py              enquiry + contact forms (no models)
  captcha.py            stateless signed CAPTCHA
  context_processors.py header / nav / footer
  templatetags/         split_heading, tel_href, is_current
templates/
  base.html
  includes/             topbar, header, marquee, nav, footer, hero, form, icons
  pages/                one template per page
static/
  css/main.css          the whole theme
  js/main.js            carousels, menu, form, video facades
  img/                  slides, schools, events, people, partners, logos
```

---

## Pages

| URL | What it is |
| --- | --- |
| `/` | Homepage — hero video, notice board, welcome, enquiry, enlistments, offerings, schools, videos, events, chancellor, testimonials |
| `/academics/schools/` · `/academics/schools/<slug>/` | The eight schools, and each school with its courses |
| `/academics/courses/` · `/academics/courses/<slug>/` | All 27 courses, filterable by programme and school |
| `/academics/facilities/` | Campus facilities |
| `/academics/industry-partners/` | Industry collaboration |
| `/admission/` · `/admission/apply/` | Admission process, scholarships, enquiry form |
| `/events/` · `/events/<slug>/` | Events, paginated |
| `/events/notices/` · `/events/notices/<slug>/` | Notice board |
| `/page/<slug>/` | Editorial pages (About, Vision & Mission, IQAC, NIRF, WILP, …) |
| `/contact/` · `/faq/` · `/search/` | Help desk, FAQ, site search |

### JSON endpoints

Used by the enquiry form; they read from `data.py` like every other view.

* `GET /api/cities/?state=<state>` — cities for a state
* `GET /api/courses/?program=<slug>&department=<slug>` — courses for a
  programme and/or department (either filter may be omitted)
* `GET /api/captcha/` — a fresh CAPTCHA

---

## The hero video

The homepage opens on a full-height video that autoplays, loops and stays muted
(browsers refuse to autoplay anything with sound). It is configured in
`data.HERO_VIDEO`:

* **`file`** — the clip, relative to `static/`. Currently
  `img/swamibannervideonew.mp4`. This is the preferred source: no third-party
  request, and it plays silently on a loop.
* **`youtube_id`** — only used if `file` is left blank, in which case the hero
  falls back to a muted looping YouTube background.
* **`poster`** — the still shown until the first frame paints.
* **`headline`, `subtext`, `cta_label`, `cta_url`** — the overlaid caption.

To swap the clip, drop the new file into `static/img/` and change `file`.

The current video is **37 MB**, which is a lot to push before the page settles.
Worth re-encoding to roughly 1080p / 2–4 Mbps (usually 3–8 MB for a short loop)
before launch — the hero starts playing sooner and mobile visitors are not
charged for the difference.

## Responsive behaviour

Verified in headless Chrome at **320, 360, 375, 414, 425, 600, 768, 820, 991,
992, 1024, 1100, 1199, 1200, 1280, 1366, 1440 and 1920px** across 14 pages —
252 checks, no horizontal overflow at any of them. Both `documentElement` and
`body` scroll widths are asserted, because `body { overflow-x: hidden }` hides
overflow from the usual check without actually fixing it.

How the layout changes as the screen grows:

| Width | Layout |
| --- | --- |
| < 576px | Single column. Brand name wraps under the crest. `meta-list` labels stack above their values. |
| < 768px | Drawer navigation. Header trimmed to brand + one helpline number + APPLY NOW. |
| < 992px | Header rows stack and centre; hamburger still in use. |
| ≥ 992px | Full horizontal nav on one line; header on a single row. |
| ≥ 1200px | Roomier section padding. |
| ≥ 1280px | Header contact type stops shrinking (was bottoming out near 10.6px). |
| ≥ 1440px | Shell widens to 1320px. |

Four real bugs were found and fixed in the process:

1. **Brand name clipped on phones.** `white-space: nowrap` forced the name onto
   one line; at 320px it clamped to ~8px type and *still* needed 232px inside a
   90px box. It now wraps to two or three readable lines.
2. **Long email addresses and URLs** are single unbreakable tokens and set a
   floor on page width no phone could meet — `overflow-wrap: anywhere` on the
   footer contact list, `meta-list` values and prose links.
3. **The mobile header filled the entire first screen** (~470px tall at 320px,
   with the hero starting at 630px). Now ~310px with nothing removed: the two
   info blocks share a row, the four helpline numbers run in two columns, and
   the fee link, UGC link and APPLY NOW sit on one wrapping line. Every value
   in the header — all four numbers, the full address, all three calls to
   action — is visible at every width down to 320px.
4. **The hero caption was unreadable.** The ≥768px rules style it as a light
   panel with dark text, which suited the old bright banner stills but vanished
   against video. The video hero now keeps white text over the overlay gradient.
5. **The nav spilled ~10px at exactly 992px** — twelve top-level labels on one
   `nowrap` line. Horizontal padding is trimmed between 992 and 1199px.

If you add or rename top-level menu items, re-check 992px: that row is the
tightest part of the whole layout.

## The enquiry form

Works with and without JavaScript. With JS it submits in place and shows errors
against each field; without it, it posts normally and re-renders.

The dropdowns run **State → City** and **Programme + Department → Course**:
department is asked before course, and choosing either a programme or a
department narrows the course list through `/api/courses/`. The pairing is
re-checked on the server too, so a course from the wrong department is rejected
even if the request is crafted by hand.

The CAPTCHA is stateless: the answer travels with the form in a signed token
(`django.core.signing`), so it needs no session and no database.

**Submissions are validated and logged, not stored** — there is nowhere to store
them yet. `enquiry_submit` in `views.py` is where saving or emailing goes when
the model exists.

---

## Before going live

* Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0` and `DJANGO_ALLOWED_HOSTS`.
* Run `python manage.py collectstatic` and serve `/staticfiles/`.
* Replace the placeholder toll-free number in `data.py` (`SITE["toll_free"]`)
  with the real one, and check the phone numbers and addresses.
* Swap the two demo YouTube IDs in `data.VIDEOS` for real university videos.
* Partner names in `data.PARTNERS` are placeholders pending the real list.
* Re-encode the hero video (see above) and serve it from a host that supports
  range requests — nginx and WhiteNoise both do; Django's dev server does not.
