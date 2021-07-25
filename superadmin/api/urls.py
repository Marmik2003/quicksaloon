from django.urls import path
from .views.manage_shop import ApiShopListView, CreateShopView, ManageShopView

app_name = 'superadmin_api'

urlpatterns = [
    path('shop/list_all/', ApiShopListView.as_view(), name='list_shops'),
    path('shop/create/', CreateShopView.as_view(), name='create_shop'),
    path('shop/<int:pk>/', ManageShopView.as_view(), name='manage_shop'),
]
