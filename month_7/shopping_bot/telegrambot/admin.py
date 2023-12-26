from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(UserModel)
admin.site.register(ProductModel)
admin.site.register(OrderModel)
admin.site.register(OrderitemModel)
admin.site.register(LocationModel)


