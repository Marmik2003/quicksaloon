from django.conf.urls import url
from django.urls import path, include
from . import views
# from django.contrib.auth import views as auth_views

app_name = 'public'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='user_login'),
    path('register', views.user_reg, name='user_reg'),
    path('forgot_pwd', views.forgot_pwd, name='forgot_pwd'),

]
