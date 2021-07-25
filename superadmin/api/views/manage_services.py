from rest_framework import generics, authentication, permissions

from shopadmin.models import Service, ServiceImage
from superadmin.api.serializers.service_serializers import CreateServiceSerializer, ListServiceSerializer, \
    ServiceImageSerializer, CreateServiceImageSerializer


class CreateServiceView(generics.CreateAPIView):
    """Create a new service"""
    serializer_class = CreateServiceSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class ListServicesView(generics.ListAPIView):
    """List all services"""
    queryset = Service.objects.all()
    serializer_class = ListServiceSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class ManageServiceView(generics.RetrieveUpdateAPIView):
    """Manage the service"""
    serializer_class = CreateServiceSerializer
    queryset = Service.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return shop"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(ManageServiceView, self).get_object()


class DeleteServiceView(generics.DestroyAPIView):
    """Delete the service"""
    serializer_class = CreateServiceSerializer
    queryset = Service.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return shop"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(DeleteServiceView, self).get_object()


class CreateServiceImageView(generics.CreateAPIView):
    serializer_class = CreateServiceImageSerializer
    queryset = ServiceImage.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class DeleteServiceImageView(generics.DestroyAPIView):
    serializer_class = ServiceImageSerializer
    queryset = ServiceImage.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
