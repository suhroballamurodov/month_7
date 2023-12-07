from django.db import models

# Create your models here.

class Avto(models.Model):
    egasi = models.CharField(max_length=20, default='Suhrob', verbose_name='Egasi')
    model = models.CharField(max_length=30, default='BMW X6',verbose_name='Model')
    narxi = models.IntegerField(default=500000, verbose_name='Narxi')
    rasmi = models.ImageField(upload_to='images/', blank=True, verbose_name='Rasmi')