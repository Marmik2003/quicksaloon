from rest_framework import serializers

from shopadmin.models import SubService, SubServiceImage


class CreateServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubServiceImage
        fields = ['image', 'subservice']


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubServiceImage
        fields = ['image']


class ListServiceSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(source='subserviceimage_set', many=True)

    class Meta:
        model = SubService
        fields = ['pk', 'name', 'description', 'images', 'price', 'main_service']


class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = ['name', 'description', 'main_service', 'price', 'approx_time', 'is_active']
