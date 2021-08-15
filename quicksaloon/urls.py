from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from quicksaloon import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Quicksaloon API",
        default_version='1.0.0',
        description="Quicksaloon API, created by <a href='https://thedataboy.com/'>TheDataBoy</a> with "
                    "<a href='https://4itsol.com/'>4IT Solutions</a>",
        contact=openapi.Contact(email="marmikpatel250@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

                  path('admin/', admin.site.urls),
                  path('superadmin', include('superadmin.urls')),
                  # path('', include('public.urls')),

                  # API URLS
                  path('api/', include('public.api.urls')),
                  path('superadmin/api/', include('superadmin.api.urls')),
                  path('shopadmin/api/', include('shopadmin.api.urls')),
                  path('customer/api/', include('customer.api.urls')),
                  path('barber/api/', include('barber.api.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
