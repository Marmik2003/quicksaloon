from rest_framework import generics, authentication, permissions, status
from rest_framework.response import Response

from public.models import Barber
from shopadmin.api.serializers.barber_serializers import BarberSerializer
from shopadmin.api.views.manage_branches import IsShopAdmin


class CreateBarberView(generics.CreateAPIView):
    """Create a new barber type user"""
    serializer_class = BarberSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin)

    def perform_create(self, serializer):
        serializer.save(mainshop=self.request.user.shopadmin.shop)


class ListAllBarbersView(generics.ListAPIView):
    """List all barbers"""
    serializer_class = BarberSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin or permissions.IsAdminUser)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return Barber.objects.filter(shop__mainshop__shopadmin__user=self.request.user)
        elif self.request.user.is_superuser:
            return Barber.objects.all()
        else:
            return Barber.objects.none()


class ListBarbersPerBranchView(generics.ListAPIView):
    """List all barbers"""
    serializer_class = BarberSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin or permissions.IsAdminUser)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            if 'shop_id' in self.kwargs:
                return Barber.objects.filter(
                    shop__mainshop__shopadmin__user=self.request.user,
                    shop_id=self.kwargs['shop_id']
                )
        elif self.request.user.is_superuser:
            return Barber.objects.filter(
                shop_id=self.kwargs['shop_id']
            )
        else:
            return Barber.objects.none()


class ManageBarberView(generics.RetrieveUpdateAPIView):
    """Manage the barber"""
    serializer_class = BarberSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin or permissions.IsAdminUser)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return Barber.objects.filter(shop__mainshop__shopadmin__user=self.request.user)
        elif self.request.user.is_superuser:
            return Barber.objects.all()
        else:
            return Barber.objects.none()

    def get_object(self):
        """Retrieve and return barber"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(ManageBarberView, self).get_object()


class DeleteBarberView(generics.DestroyAPIView):
    """Delete the barber"""
    serializer_class = BarberSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsShopAdmin or permissions.IsAdminUser)

    def get_queryset(self):
        if self.request.user.is_shopadmin:
            return Barber.objects.filter(shop__mainshop__shopadmin__user=self.request.user)
        elif self.request.user.is_superuser:
            return Barber.objects.all()
        else:
            return Barber.objects.none()

    def get_object(self):
        """Retrieve and return barber"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(DeleteBarberView, self).get_object()

    def destroy(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            Barber.objects.get(id=self.kwargs['pk']).user.delete()
            return Response("Barber deleted successfully", status=status.HTTP_204_NO_CONTENT)
