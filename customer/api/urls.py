from django.urls import path

from .views.order_views import CreateOrderAPIView, ListCurrentOrdersView
from .views.shop_views import ApiShopListView, GetShopDetailsView, ShopRatingList, AddReviewApi, EditReviewView

app_name = 'customer_api'

urlpatterns = [
    path('shop/list_all/', ApiShopListView.as_view(), name='list_shops'),
    path('shop/<int:pk>/', GetShopDetailsView.as_view(), name='get_shop'),

    path('ratings/<int:shop_id>/', ShopRatingList.as_view()),
    path('ratings/add/', AddReviewApi.as_view()),
    path('ratings/edit/<int:pk>/', EditReviewView.as_view()),

    path('orders/create/', CreateOrderAPIView.as_view()),
    path('orders/current/', ListCurrentOrdersView.as_view()),
]
