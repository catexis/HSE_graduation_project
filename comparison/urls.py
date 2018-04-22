from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^vergleich/', include('vergleich.urls')),
    # Redirect to main page
    url(r'^$', RedirectView.as_view(url='/vergleich/', permanent=True)),
    # Login pages
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
# Static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
