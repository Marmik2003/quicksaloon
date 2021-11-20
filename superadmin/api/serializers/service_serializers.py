from rest_framework import serializers

from shopadmin.models import ServiceImage, Service


class CreateServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        ref_name = "AdminCreateServiceImage"
        fields = ['image', 'service']


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        ref_name = "AdminServiceImage"
        fields = ['image']


class ListServiceSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(source='serviceimage_set', many=True)

    class Meta:
        model = Service
        ref_name = "AdminServiceList"
        fields = ['pk', 'name', 'description', 'images', 'is_active']


class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        ref_name = "AdminService"
        fields = ['name', 'description', 'is_active']
