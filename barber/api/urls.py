from django.urls import path

from .views.order_views import CreateOrderAPIView, ListCurrentOrdersView, finish_order, reject_order, \
    GetMonthlyOrderReport, GetWeeklyOrderReport

app_name = 'barber_api'

urlpatterns = [
    path('orders/create/', CreateOrderAPIView.as_view()),
    path('orders/current/', ListCurrentOrdersView.as_view()),
    path('orders/finish/<int:order_id>/', finish_order),
    path('orders/reject/<int:order_id>/', reject_order),
    path('orders/monthly/', GetMonthlyOrderReport.as_view()),
    path('orders/weekly/', GetWeeklyOrderReport.as_view()),
]
