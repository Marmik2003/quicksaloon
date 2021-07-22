from django.conf.urls import url
from django.urls import path, include
from .views import dashboard
# from django.contrib.auth import views as auth_views

app_name = 'superadmin'

urlpatterns = [
    path('', dashboard.dashboard, name='dashboard'),

]
