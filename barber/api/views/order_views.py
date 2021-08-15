from datetime import timedelta

from django.utils import timezone
from rest_framework import generics, authentication, permissions, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from customer.api.serializers.order_serializers import OrderSerializer, ListOrderSerializer
from customer.models import Order


class IsBarber(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_barber


class CreateOrderAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class ListCurrentOrdersView(generics.ListAPIView):
    serializer_class = ListOrderSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(barber=self.request.user.barber,
                                    booking_time__gte=(timezone.now()
                                                       - timedelta(days=1))).order_by('-booking_time')


@api_view(['POST'])
@authentication_classes((authentication.TokenAuthentication,))
@permission_classes((permissions.IsAuthenticated, IsBarber))
def finish_order(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(id=order_id)
        order.order_finished = True
        order.save()
        data = {'order_id': order_id, 'response': 'Order finished successfully!'}
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes((authentication.TokenAuthentication,))
@permission_classes((permissions.IsAuthenticated, IsBarber))
def reject_order(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(id=order_id)
        order.order_rejected = True
        order.save()
        data = {'order_id': order_id, 'response': 'Order rejected successfully!'}
        return Response(data=data, status=status.HTTP_200_OK)


class GetMonthlyOrderReport(generics.ListAPIView):
    serializer_class = ListOrderSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsBarber)
    pagination_class = PageNumberPagination
    paginate_by = 25

    def get_queryset(self):
        return Order.objects.filter(barber=self.request.user.barber,
                                    booking_time__gte=(timezone.now()
                                                       - timedelta(days=30))).order_by('-booking_time')


class GetWeeklyOrderReport(generics.ListAPIView):
    serializer_class = ListOrderSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsBarber)
    pagination_class = PageNumberPagination
    paginate_by = 25

    def get_queryset(self):
        return Order.objects.filter(barber=self.request.user.barber,
                                    booking_time__gte=(timezone.now()
                                                       - timedelta(days=7))).order_by('-booking_time')
