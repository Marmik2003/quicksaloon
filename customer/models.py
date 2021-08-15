from django.db import models

# Create your models here.
from simple_history.models import HistoricalRecords

from public.models import User, Barber


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=15)
    shop = models.ForeignKey('shopadmin.ShopBranch', on_delete=models.SET_NULL, null=True)
    subservices = models.ManyToManyField('shopadmin.SubService')
    customer = models.ForeignKey('public.User', on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField(default=0)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=40, null=True, blank=True)
    order_finished = models.BooleanField(default=False)
    order_rejected = models.BooleanField(default=False)
    booking_time = models.DateTimeField(auto_now_add=True)
    et_finish = models.PositiveIntegerField(default=0)
    at_finish = models.PositiveIntegerField(default=0)
    et_order = models.PositiveIntegerField(default=0)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class UserRatings(models.Model):
    user = models.ForeignKey('public.User', on_delete=models.CASCADE, blank=True)
    shop = models.ForeignKey('shopadmin.ShopBranch', on_delete=models.CASCADE)
    barber = models.ForeignKey('public.Barber', on_delete=models.CASCADE, null=True)
    rating = models.PositiveSmallIntegerField()
    review = models.TextField(blank=True, null=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'User Ratings'
        unique_together = (('user', 'shop'),)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

