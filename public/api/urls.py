from django.urls import path
from .views.user_views import CreateUserView, CreateTokenView, ManageUserView

app_name = 'public_api'

urlpatterns = [
    path('users/create/', CreateUserView.as_view(), name='create'),
    path('users/token/', CreateTokenView.as_view(), name='token'),
    path('users/me/', ManageUserView.as_view(), name='me'),
]
