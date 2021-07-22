from django.db import models

# Create your models here.
from simple_history.models import HistoricalRecords


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=15)
    shop = models.ForeignKey('shopadmin.ShopBranch', on_delete=models.SET_NULL, null=True)
    services = models.ManyToManyField('shopadmin.Service')
    subservices = models.ManyToManyField('shopadmin.SubService')
    customer_id = models.ForeignKey('public.User', on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField(default=0)
    order_status = models.CharField(max_length=40)
    order_finished = models.BooleanField(default=False)
    order_rejected = models.BooleanField(default=False)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class UserRatings(models.Model):
    user = models.ForeignKey('public.User', on_delete=models.CASCADE)
    shop = models.ForeignKey('shopadmin.ShopBranch', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    review = models.TextField()
    history = HistoricalRecords()

    class Meta:
        unique_together = (('user', 'shop'),)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

