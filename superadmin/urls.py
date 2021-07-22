from django.conf.urls import url
from django.urls import path, include
from . import views
# from django.contrib.auth import views as auth_views

app_name = 'superadmin'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

]
