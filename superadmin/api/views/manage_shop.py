from rest_framework import permissions, authentication, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination

from shopadmin.models import MainShop
from superadmin.api.serializers.shop_serializers import ShopSerializer, CreateShopSerializer, ManageShopSerializer


class ApiShopListView(generics.ListAPIView):
    queryset = MainShop.objects.filter(is_active=True)
    serializer_class = ShopSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('shop_name', 'subscription', 'main_branch__branch_name',
                     'main_branch__address')


class CreateShopView(generics.CreateAPIView):
    """Create a new shop"""
    serializer_class = CreateShopSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class ManageShopView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = ManageShopSerializer
    queryset = MainShop.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return shop"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(ManageShopView, self).get_object()
