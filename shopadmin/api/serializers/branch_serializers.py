from rest_framework import serializers

from shopadmin.models import ShopBranch


class ShopBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopBranch
        fields = ['branch_name', 'opening_time', 'closing_time', 'address',
                  'latitude', 'longitude', 'main_image']

