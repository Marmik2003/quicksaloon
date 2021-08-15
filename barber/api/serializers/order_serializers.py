from rest_framework import serializers

from customer.models import UserRatings
from public.models import User
from customer.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['subservices', 'customer_name']


class ListOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['pk', 'subservices', 'customer_name',
                  'amount', 'order_status',
                  'order_finished', 'order_rejected',
                  'et_finish', 'et_order']
