"""Root URL configuration — everything lives in the ``website`` app."""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("", include("website.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "static")

handler404 = "website.views.error_404"
handler500 = "website.views.error_500"
