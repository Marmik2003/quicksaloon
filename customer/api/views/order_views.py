from rest_framework import generics, authentication, permissions, status
from rest_framework.response import Response

from customer.api.serializers.order_serializers import OrderSerializer, ListOrderSerializer
from customer.models import Order
from public.models import User
from shopadmin.models import SubService, ShopBranch


class CreateOrderAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        order = Order(customer=self.request.user,
                      customer_name=self.request.user.get_full_name(),
                      customer_phone=self.request.user.phone)
        subservice_ids = request.data['subservices']
        amount = 0
        et_finish = 0
        for subservice_id in subservice_ids:
            subservice = SubService.objects.get(id=subservice_id)
            amount += subservice.price
            et_finish += subservice.approx_time
        et_order = 0
        for running_order in Order.objects.filter(shop__id=request.data['shop'], barber__id=request.data['barber'],
                                                  order_finished=False, order_rejected=False):
            et_order += running_order.et_finish

        order.amount = amount
        order.et_order = et_order
        order.et_finish = et_finish
        serializer = self.serializer_class(order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {'et_order': et_order, 'et_finish': et_finish, 'amount': amount,
                    'subservices': serializer.data['subservices'],
                    'barber': User.objects.get(barber__id=serializer.data['barber']).get_full_name(),
                    'shop': str(ShopBranch.objects.get(id=serializer.data['shop']))}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCurrentOrdersView(generics.ListAPIView):
    serializer_class = ListOrderSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user, order_finished=False, order_rejected=False)
