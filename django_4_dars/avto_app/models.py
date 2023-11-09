from django.db import models

# Create your models here.

class Avto(models.Model):
    sarlavha = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    model = models.TextField(max_length=100)
    year = models.IntegerField(default=2022)
    price = models.IntegerField()
    auto_pictures = models.ImageField(upload_to='photos/%Y/%m/%d', default='Mashina rasmi mavjud emas')

def __str__(self):
    return self.model

class Meta:
    verbose_name = 'Mashinalar haqida'