from rest_framework import serializers

from shopadmin.models import ServiceImage, Service


class CreateServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ['image', 'service']


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ['image']


class ListServiceSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(source='serviceimage_set', many=True)

    class Meta:
        model = Service
        fields = ['pk', 'name', 'description', 'images']


class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'description']
