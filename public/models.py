from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from simple_history.models import HistoricalRecords


class User(AbstractUser):
    is_barber = models.BooleanField(default=False)
    is_shopadmin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=(
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Whether not to say')
    ))


class ShopAdmin(models.Model):
    shop = models.OneToOneField('shopadmin.MainShop', on_delete=models.CASCADE, primary_key=True)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Barber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shop = models.ForeignKey('shopadmin.ShopBranch', on_delete=models.SET_NULL, null=True)
    is_offerprovider = models.BooleanField(default=False)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
