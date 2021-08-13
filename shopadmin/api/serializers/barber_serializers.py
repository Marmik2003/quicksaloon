from django.db import transaction
from rest_framework import serializers

from public.api.serializers.user_serializers import UserSerializer
from public.models import Barber, User


class BarberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Barber
        fields = ['id', 'shop', 'user']

    @transaction.atomic
    def save(self, **kwargs):
        try:
            barber_user = User.objects.create_user(
                phone=self.validated_data['user']['phone'],
                email=self.validated_data['user']['email'],
                first_name=self.validated_data['user']['first_name'],
                password=self.validated_data['user']['password']
            )
            barber_user.is_barber = True
            barber_user.save()
            barber = Barber.objects.create(
                shop=self.validated_data['shop'],
                user=barber_user
            )

            return barber
        except KeyError:
            raise serializers.ValidationError({"response": "You must have a shop id and user object containing "
                                                           "phone, password, email and first name."})
