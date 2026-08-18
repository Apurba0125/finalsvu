"""
Settings for the Swami Vivekananda University front end.

This build is deliberately front-end only: there is no database, no models and
no admin panel.  Every page is rendered from ``website/data.py`` through
``website/views.py``.  That keeps the whole site in plain Python while the
content is still being decided.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# In production set DJANGO_SECRET_KEY in the environment.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "dev-only-key-change-me-before-going-live-0f2a7c91b4e6",
)

DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"

ALLOWED_HOSTS = [
    h.strip()
    for h in os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,[::1]").split(",")
    if h.strip()
]

CSRF_TRUSTED_ORIGINS = [
    o.strip()
    for o in os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")
    if o.strip()
]

# Render publishes the service's own hostname here.  Trusting it automatically
# means a fresh deploy answers on its .onrender.com address without anyone
# having to copy that name into an environment variable first.
RENDER_HOST = os.environ.get("RENDER_EXTERNAL_HOSTNAME", "").strip()
if RENDER_HOST:
    if RENDER_HOST not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(RENDER_HOST)
    origin = "https://%s" % RENDER_HOST
    if origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(origin)


INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "website",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # Must sit directly after SecurityMiddleware: it answers requests for
    # /static/ itself, so the site needs no separate static host in production.
    # In DEBUG the runserver still serves static files, so this is a no-op then.
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                # Header, navigation and footer content for every page.
                "website.context_processors.site_context",
            ],
            "builtins": ["website.templatetags.svu_extras"],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# No models are defined, so no database connection is configured.
DATABASES = {}

LANGUAGE_CODE = "en-in"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise stamps a content hash into each filename at collectstatic time and
# serves them with a long cache life.  Editing main.css or main.js therefore
# changes its URL, so a browser can never keep showing a stale copy.
if not DEBUG:
    STORAGES = {
        "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Security ---------------------------------------------------------------
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"
X_FRAME_OPTIONS = "DENY"

if not DEBUG:
    # Render terminates TLS at its proxy and forwards plain HTTP, so without
    # this Django believes every request is insecure and SECURE_SSL_REDIRECT
    # below sends the browser round an endless redirect loop.
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
