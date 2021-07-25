from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from quicksaloon import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('superadmin', include('superadmin.urls')),
    path('', include('public.urls')),

    # API URLS
    path('api/', include('public.api.urls')),
    path('superadmin/api/', include('superadmin.api.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)