from rest_framework import generics, authentication, permissions

from shopadmin.api.serializers.branch_serializers import ShopBranchSerializer
from shopadmin.models import ShopBranch


# permissions
class IsShopAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_shopadmin


# Main Views

class CreateShopBranchView(generics.CreateAPIView):
    """Create a new shop branch"""
    serializer_class = ShopBranchSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def perform_create(self, serializer):
        serializer.save(mainshop=self.request.user.shopadmin.shop)


class ListAllShopBranchesView(generics.ListAPIView):
    """List all shop branches"""
    serializer_class = ShopBranchSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin or permissions.IsAdminUser)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return ShopBranch.objects.filter(mainshop__shopadmin__user=self.request.user)
        elif self.request.user.is_superuser:
            return ShopBranch.objects.all()
        else:
            return ShopBranch.objects.none()


class ManageShopBranchView(generics.RetrieveUpdateAPIView):
    """Manage the shop branch"""
    serializer_class = ShopBranchSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin or permissions.IsAdminUser)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return ShopBranch.objects.filter(mainshop__shopadmin__user=self.request.user)
        elif self.request.user.is_superuser:
            return ShopBranch.objects.all()
        else:
            return ShopBranch.objects.none()

    def get_object(self):
        """Retrieve and return shop branch"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(ManageShopBranchView, self).get_object()


class DeleteShopBranchView(generics.DestroyAPIView):
    """Delete the shop branch"""
    serializer_class = ShopBranchSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin or permissions.IsAdminUser)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return ShopBranch.objects.filter(mainshop__shopadmin__user=self.request.user)
        elif self.request.user.is_superuser:
            return ShopBranch.objects.all()
        else:
            return ShopBranch.objects.none()

    def get_object(self):
        """Retrieve and return shop branch"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(DeleteShopBranchView, self).get_object()
