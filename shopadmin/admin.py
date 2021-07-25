from django.contrib import admin

# Register your models here.
from shopadmin.models import MainShop, ShopBranch, ShopImage

admin.site.register(MainShop)
admin.site.register(ShopBranch)
admin.site.register(ShopImage)
