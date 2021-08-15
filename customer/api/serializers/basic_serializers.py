from rest_framework import serializers

from customer.models import UserRatings, Order
from public.models import User, Barber
from shopadmin.models import MainShop, ShopImage, ShopBranch


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        ref_name = "UserInfoSerializer"
        fields = ('first_name', 'last_name', 'avatar')


class ShopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopImage
        fields = ['image', 'user']


class BarberSerializer(serializers.ModelSerializer):
    barber_name = serializers.SerializerMethodField('get_fullname_barber')
    estimated_time = serializers.SerializerMethodField('get_barber_et')
    pending_orders = serializers.SerializerMethodField('get_pending_orders')

    class Meta:
        model = Barber
        ref_name = "CustomBarberSerializer"
        fields = ['barber_name', 'estimated_time', 'pending_orders']

    @staticmethod
    def get_fullname_barber(barber):
        barber_name = barber.user.get_full_name()
        return barber_name

    @staticmethod
    def get_barber_et(barber):
        active_orders = Order.objects.filter(barber=barber, order_finished=False, order_rejected=False)
        estimated_time = 0
        for order in active_orders:
            estimated_time += order.et_finish
        return estimated_time

    @staticmethod
    def get_pending_orders(barber):
        return len(Order.objects.filter(barber=barber, order_rejected=False, order_finished=False))


class ShopBranchSerializer(serializers.ModelSerializer):
    images = ShopImageSerializer(source='shopimage_set', many=True)
    barbers = BarberSerializer(source='barber_set', many=True)

    class Meta:
        model = ShopBranch
        ref_name = "CustomShopBranchSerializer"
        fields = ['pk', 'branch_name', 'images', 'barbers']


class ShopSerializer(serializers.ModelSerializer):
    branches = ShopBranchSerializer(source='shopbranch_set', many=True)
    main_branch = ShopBranchSerializer()

    class Meta:
        model = MainShop
        ref_name = "CustomShop"
        fields = ['pk', 'shop_name', 'main_branch', 'branches']


class BarberNameSerializer(serializers.ModelSerializer):
    barber_name = serializers.SerializerMethodField('get_fullname_barber')

    class Meta:
        model = Barber
        fields = ['barber_name']

    @staticmethod
    def get_fullname_barber(barber):
        barber_name = barber.user.get_full_name()
        return barber_name


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    barber = BarberSerializer()

    class Meta:
        model = UserRatings
        fields = ['user', 'rating', 'review', 'barber']


class AddRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRatings
        fields = ['rating', 'review', 'shop', 'barber']
