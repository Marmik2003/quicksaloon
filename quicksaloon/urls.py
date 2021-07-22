from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('superadmin', include('superadmin.urls')),
    path('', include('public.urls')),
]
