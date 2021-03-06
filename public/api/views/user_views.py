from rest_framework import generics, authentication, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.settings import api_settings

from public.api.serializers.user_serializers import UserSerializer, AuthTokenSerializer, UserPropertiesSerializer
from public.models import User


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_object = token.user
        return Response({
            'token': token.key,
            'user_id': user_object.pk,
            'phone': user_object.phone,
            'first_name': user_object.first_name,
            'last_name': user_object.last_name,
            'is_barber': user_object.is_barber,
            'is_shopadmin': user_object.is_shopadmin,
            'is_superuser': user_object.is_superuser,
        })


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return get_object_or_404(User, phone=self.request.user.phone)


@api_view(['GET', ])
@permission_classes((permissions.IsAuthenticated,))
@authentication_classes((authentication.TokenAuthentication,),)
def user_properties_view(request):
    try:
        user = request.user
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserPropertiesSerializer(user)
        return Response(serializer.data)
