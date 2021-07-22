from django.db import models

# Create your models here.
from simple_history.models import HistoricalRecords


class MainShop(models.Model):
    shop_name = models.CharField(max_length=255)
    subscription = models.CharField(
        max_length=25,
        choices=(
            (1, 'Free'),
            (2, 'Basic'),
            (3, 'Gold'),
            (4, 'Platinum'),
            (5, 'Diamond'),
            (6, 'Full Access')
        )
    )

    # shop_admin = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    main_branch = models.OneToOneField('shopadmin.ShopBranch', on_delete=models.SET_NULL, null=True,
                                       related_name='shop_branch')
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class ShopSubscription(models.Model):
    shop = models.ForeignKey(MainShop, on_delete=models.SET_NULL, null=True)
    subscription_start_date = models.DateField()
    subscription_end_date = models.DateField()
    subscription_type = models.CharField(
        max_length=25,
        choices=(
            (1, 'Free'),
            (2, 'Basic'),
            (3, 'Gold'),
            (4, 'Platinum'),
            (5, 'Diamond'),
            (6, 'Full Access')
        )
    )

    def __str__(self):
        return self.shop + ' - ' + self.subscription_type


class ShopBranch(models.Model):
    branch_name = models.CharField(max_length=384)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    mainshop = models.ForeignKey(MainShop, on_delete=models.CASCADE)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class ShopImage(models.Model):
    shop = models.ForeignKey(ShopBranch, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shops/')
    user = models.ForeignKey('public.User', on_delete=models.SET_NULL, null=True)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class ShopHoliday(models.Model):
    shop = models.ForeignKey(ShopBranch, on_delete=models.SET_NULL, null=True)
    mainshop = models.ForeignKey(MainShop, on_delete=models.CASCADE)
    date = models.DateField()
    holiday_allbranch = models.BooleanField(default=False)


class Service(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service/')


class SubService(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    main_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    main_shop = models.ForeignKey(MainShop, on_delete=models.CASCADE)
    shops = models.ManyToManyField(ShopBranch)
    price = models.PositiveIntegerField()
    approx_time = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class SubServiceImage(models.Model):
    subservice = models.ForeignKey(SubService, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subservice/')


class Offering(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    main_shop = models.ForeignKey(MainShop, on_delete=models.CASCADE, null=True)
    shops = models.ManyToManyField(ShopBranch)
    from_date = models.DateField()
    to_date = models.DateField()
    for_allshop = models.BooleanField(default=False)
