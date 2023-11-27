from django.db import models

# Create your models here.


class MatheModel(models.Model):
    birinchi_son = models.IntegerField(default=13, verbose_name='Birinchi son')
    ikkinchi_son = models.IntegerField(default=15, verbose_name='Ikkinchi son')
    natija = models.IntegerField(default=28, verbose_name='Natija')

    def __str__(self) -> str:
        return str(self.natija)
        
    class Meta:
        verbose_name = 'Misol'
        verbose_name_plural = 'Misollar'

class TestModel(models.Model):
    savol = models.TextField(default="13 + 24 nechchi bo'ladi ?")
    a = models.IntegerField(default=27)
    b = models.IntegerField(default=56)
    c = models.IntegerField(default=68)
    rasm = models.ImageField(null=True, blank=True, verbose_name='Test rasmi')

    def __str__(self) -> str:
        return self.savol



    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tetslar'