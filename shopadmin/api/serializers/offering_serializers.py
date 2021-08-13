from rest_framework import serializers

from shopadmin.models import Offering


class ListOfferingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offering
        fields = ['pk', 'name', 'description',
                  'from_date', 'to_date',
                  'for_allshop', 'shops', 'subservices']


class CreateOfferingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offering
        fields = ['name', 'description', 'from_date',
                  'to_date', 'offer_code', 'for_allshop',
                  'shops', 'special_offer', 'subservices']
