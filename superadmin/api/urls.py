from django.urls import path

from .views.manage_shop import ApiShopListView, CreateShopView, ManageShopView, DeleteShopView
from .views.manage_services import ListServicesView, CreateServiceView, ManageServiceView, DeleteServiceView, \
    CreateServiceImageView, DeleteServiceImageView

app_name = 'superadmin_api'

urlpatterns = [
    path('shop/list_all/', ApiShopListView.as_view(), name='list_shops'),
    path('shop/create/', CreateShopView.as_view(), name='create_shop'),
    path('shop/<int:pk>/', ManageShopView.as_view(), name='manage_shop'),
    path('shop/delete/<int:pk>/', DeleteShopView.as_view(), name='delete_shop'),

    path('services/', ListServicesView.as_view(), name='list_services'),
    path('services/create/', CreateServiceView.as_view(), name='create_service'),
    path('service/<int:pk>/', ManageServiceView.as_view(), name='manage_service'),
    path('service/delete/<int:pk>/', DeleteServiceView.as_view(), name='delete_service'),

    path('service/image/', CreateServiceImageView.as_view(), name='add_service_image'),
    path('service/image/<int:pk>/', DeleteServiceImageView.as_view(), name='delete_service_image'),
]
