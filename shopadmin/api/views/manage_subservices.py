from rest_framework import generics, authentication, permissions

from shopadmin.models import SubService, SubServiceImage
from shopadmin.api.serializers.subservice_serializers import CreateServiceSerializer, ListServiceSerializer, \
    ServiceImageSerializer, CreateServiceImageSerializer


# permissions
class IsShopAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_shopadmin


class CreateServiceView(generics.CreateAPIView):
    """Create a new service"""
    serializer_class = CreateServiceSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def perform_create(self, serializer):
        serializer.save(main_shop=self.request.user.shopadmin.shop)


class ListServicesView(generics.ListAPIView):
    """List all services"""
    serializer_class = ListServiceSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return SubService.objects.filter(main_shop__shopadmin__user=self.request.user)


class ManageServiceView(generics.RetrieveUpdateAPIView):
    """Manage the service"""
    serializer_class = CreateServiceSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return SubService.objects.filter(main_shop__shopadmin__user=self.request.user)

    def get_object(self):
        """Retrieve and return shop"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(ManageServiceView, self).get_object()


class DeleteServiceView(generics.DestroyAPIView):
    """Delete the service"""
    serializer_class = CreateServiceSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return SubService.objects.filter(main_shop__shopadmin__user=self.request.user)

    def get_object(self):
        """Retrieve and return services"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(DeleteServiceView, self).get_object()


class CreateServiceImageView(generics.CreateAPIView):
    serializer_class = CreateServiceImageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return SubServiceImage.objects.filter(subservice__main_shop__shopadmin__user=self.request.user)


class DeleteServiceImageView(generics.DestroyAPIView):
    serializer_class = ServiceImageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return SubServiceImage.objects.filter(subservice__main_shop__shopadmin__user=self.request.user)
