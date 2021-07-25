import json

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from shopadmin.models import MainShop, ShopBranch
from superadmin.api.serializers.shop_serializers import ShopSerializer

LIST_SHOPS_URL = reverse('superadmin_api:list_shops')
CREATE_SHOP_URL = reverse('superadmin_api:create_shop')


def create_superuser(**params):
    return get_user_model().objects.create_superuser(**params)


class PrivateUserApiTests(TestCase):
    """Test API requests that require superuser"""

    def setUp(self):
        self.user = create_superuser(
            email='tes111t@test.com',
            password='test123',
            first_name='testname',
            phone='+12221212',
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_shops_list(self):
        """Test retrieving a list of shops"""
        main_shop1 = MainShop.objects.create(shop_name='Shop 1', subscription='Free')
        shop_branch1 = ShopBranch.objects.create(branch_name='mainbranch1', address='address1', mainshop=main_shop1)
        main_shop2 = MainShop.objects.create(shop_name='Shop 2', subscription='Gold')
        main_shop1.main_branch = shop_branch1
        main_shop1.save()
        shop_branch2 = ShopBranch.objects.create(branch_name='mainbranch2', address='address2', mainshop=main_shop2)
        main_shop2.main_branch = shop_branch2
        main_shop2.save()

        res = self.client.get(LIST_SHOPS_URL)

        main_shops = MainShop.objects.all().order_by('shop_name')
        serializer = ShopSerializer(main_shops, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_valid_main_shop_success(self):
        """Test creating shop with valid payload"""
        payload = {
            "shop_name": "testing abc 123",
            "subscription": "Free",
            "main_branch": {
                "branch_name": "testing branch 123",
                "address": "abc abc abc 123 123 123"
            }
        }
        res = self.client.post(CREATE_SHOP_URL,
                               json.dumps(payload),
                               content_type="application/json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        exists = MainShop.objects.filter(
            shop_name="testing abc 123", subscription="Free"
        ).exists()
        self.assertTrue(exists)
