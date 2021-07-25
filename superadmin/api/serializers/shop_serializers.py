from rest_framework import serializers

from shopadmin.models import MainShop, ShopImage, ShopBranch


class ShopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopImage
        fields = ['image', 'user']


class ShopBranchSerializer(serializers.ModelSerializer):
    images = ShopImageSerializer(source='shopimage_set', many=True)

    class Meta:
        model = ShopBranch
        fields = ['branch_name', 'images']


class ShopSerializer(serializers.ModelSerializer):
    branches = ShopBranchSerializer(source='shopbranch_set', many=True)

    class Meta:
        model = MainShop
        fields = ['pk', 'shop_name', 'subscription', 'main_branch', 'branches']


class CreateMainBranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopBranch
        fields = ['branch_name', 'address', 'latitude', 'longitude']


class CreateShopSerializer(serializers.ModelSerializer):
    main_branch = CreateMainBranchSerializer()

    class Meta:
        model = MainShop
        fields = ['shop_name', 'subscription', 'main_branch']

    def save(self):
        try:

            main_shop = MainShop.objects.create(
                shop_name=self.validated_data['shop_name'],
                subscription=self.validated_data['subscription']
            )

            main_branch = ShopBranch.objects.create(
                branch_name=self.validated_data['main_branch']['branch_name'],
                address=self.validated_data['main_branch']['address'],
                mainshop=main_shop
            )

            main_shop.main_branch = main_branch
            main_shop.save()

            return main_shop
        except KeyError:
            raise serializers.ValidationError({"response": "You must have a shop name, subscription, main branch name "
                                                           "and address."})


class ManageShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainShop
        fields = ['shop_name', 'subscription', 'is_active']
