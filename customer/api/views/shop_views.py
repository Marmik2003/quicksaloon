from rest_framework import generics, authentication, permissions, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from customer.api.serializers.basic_serializers import ShopSerializer, RatingSerializer, AddRatingSerializer
from customer.models import UserRatings
from shopadmin.models import MainShop


class ApiShopListView(generics.ListAPIView):
    queryset = MainShop.objects.filter(is_active=True)
    serializer_class = ShopSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('main_branch__branch_name', 'main_branch__address')


class GetShopDetailsView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    permission_classes = (AllowAny,)
    serializer_class = ShopSerializer
    queryset = MainShop.objects.filter(is_active=True)


class ShopRatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    paginate_by = 30

    def get_queryset(self):
        queryset = UserRatings.objects.filter(shop__id=self.kwargs['shop_id'])
        return queryset


class AddReviewApi(generics.CreateAPIView):
    serializer_class = AddRatingSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        rating = UserRatings(user=self.request.user)
        serializer = self.serializer_class(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditReviewView(generics.RetrieveUpdateAPIView):
    """Manage the rating"""
    serializer_class = AddRatingSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return UserRatings.objects.filter(user=self.request.user)

    def get_object(self):
        """Retrieve and return rating"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(EditReviewView, self).get_object()
