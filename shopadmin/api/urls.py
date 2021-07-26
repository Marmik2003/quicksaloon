from django.urls import path

from .views.manage_branches import CreateShopBranchView, ListAllShopBranchesView,\
    ManageShopBranchView, DeleteShopBranchView

app_name = 'shopadmin_api'

urlpatterns = [
    path('branch/create/', CreateShopBranchView.as_view(), name='create_branch'),
    path('branch/list/', ListAllShopBranchesView.as_view(), name='list_branches'),
    path('branch/<int:pk>/', ManageShopBranchView.as_view(), name='manage_branch'),
    path('branch/delete/<int:pk>/', DeleteShopBranchView.as_view(), name='delete_branch'),
]
