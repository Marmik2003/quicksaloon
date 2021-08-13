from django.urls import path

from .views.manage_barbers import CreateBarberView, ListAllBarbersView, ManageBarberView, DeleteBarberView, \
    ListBarbersPerBranchView
from .views.manage_branches import CreateShopBranchView, ListAllShopBranchesView,\
    ManageShopBranchView, DeleteShopBranchView
from .views.manage_offerings import ListOfferingsView, ManageOfferingView, DeleteOfferingView, CreateOfferingView
from .views.manage_subservices import ListServicesView, CreateServiceView, ManageServiceView, DeleteServiceView, \
    CreateServiceImageView, DeleteServiceImageView

app_name = 'shopadmin_api'

urlpatterns = [
    path('branch/create/', CreateShopBranchView.as_view(), name='create_branch'),
    path('branch/list/', ListAllShopBranchesView.as_view(), name='list_branches'),
    path('branch/<int:pk>/', ManageShopBranchView.as_view(), name='manage_branch'),
    path('branch/delete/<int:pk>/', DeleteShopBranchView.as_view(), name='delete_branch'),

    path('barber/add/', CreateBarberView.as_view(), name='create_barber'),
    path('barber/list/', ListAllBarbersView.as_view(), name='list_barbers'),
    path('barber/list/<int:shop_id>/', ListBarbersPerBranchView.as_view(), name='list_barbers'),
    path('barber/<int:pk>/', ManageBarberView.as_view(), name='manage_barber'),
    path('barber/delete/<int:pk>/', DeleteBarberView.as_view(), name='delete_barber'),

    path('subservices/', ListServicesView.as_view(), name='list_subservices'),
    path('subservices/create/', CreateServiceView.as_view(), name='create_subservice'),
    path('subservice/<int:pk>/', ManageServiceView.as_view(), name='manage_subservice'),
    path('subservice/delete/<int:pk>/', DeleteServiceView.as_view(), name='delete_subservice'),

    path('subservice/image/', CreateServiceImageView.as_view(), name='add_subservice_image'),
    path('subservice/image/<int:pk>/', DeleteServiceImageView.as_view(), name='delete_subservice_image'),

    path('offerings/', ListOfferingsView.as_view(), name='list_offerings'),
    path('offerings/create/', CreateOfferingView.as_view(), name='create_offering'),
    path('offering/<int:pk>/', ManageOfferingView.as_view(), name='manage_offering'),
    path('offering/delete/<int:pk>/', DeleteOfferingView.as_view(), name='delete_offering'),
]
