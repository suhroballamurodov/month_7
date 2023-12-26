from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user_id = models.IntegerField(verbose_name='User Id')
    name = models.CharField(max_length=30, verbose_name='Ismi')
    phone_number = models.CharField(max_length=15, blank=False, verbose_name='Telefon nomer')

    def __str__(self):
        return self.name
    
class ProductModel(models.Model):
    name = models.CharField(max_length=250, blank=False, verbose_name='Maxsulot nomi')
    photo = models.ImageField(null=True, blank=True,upload_to='rasmlar/', verbose_name='Rasmi')
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=False, verbose_name='Narhi')
    column_5 = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class OrderModel(models.Model):
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)

    def __str__(self):
        return self.owner and self.product

class OrderitemModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Soni')
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.product

class LocationModel(models.Model):
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    longitude = models.FloatField(verbose_name='Uzunlik')
    latitute = models.FloatField(verbose_name='Kenglik')
    
    def __str__(self):
        pass