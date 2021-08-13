from rest_framework import generics, authentication, permissions

from shopadmin.api.serializers.offering_serializers import CreateOfferingSerializer, ListOfferingSerializer
from shopadmin.models import Offering


# permissions
class IsShopAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_shopadmin


class CreateOfferingView(generics.CreateAPIView):
    """Create a new offering"""
    serializer_class = CreateOfferingSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def perform_create(self, serializer):
        serializer.save(main_shop=self.request.user.shopadmin.shop)


class ListOfferingsView(generics.ListAPIView):
    """List all offerings"""
    serializer_class = ListOfferingSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return Offering.objects.filter(main_shop__shopadmin__user=self.request.user)


class ManageOfferingView(generics.RetrieveUpdateAPIView):
    """Manage the service"""
    serializer_class = CreateOfferingSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return Offering.objects.filter(main_shop__shopadmin__user=self.request.user)

    def get_object(self):
        """Retrieve and return offerings"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(ManageOfferingView, self).get_object()


class DeleteOfferingView(generics.DestroyAPIView):
    """Delete the offering"""
    serializer_class = CreateOfferingSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return Offering.objects.filter(main_shop__shopadmin__user=self.request.user)

    def get_object(self):
        """Retrieve and return offerings"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(DeleteOfferingView, self).get_object()
