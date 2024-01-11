from django.db import models



class Brand(models.Model):
    name = models.CharField(null=False, max_length=30, verbose_name='Brand nomi')
    brand_locations = models.CharField(max_length=30, verbose_name='Brand joylashgan davlat')

    def __str__(self):
        return f"{self.name},{self.brand_locations}"
    
    class Meta:
        verbose_name = "Brand "
        verbose_name_plural = "Brandlar "


class Car(models.Model):
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30,verbose_name='Mashina nomi')
    price = models.IntegerField(verbose_name='Narxi')
    color = models.CharField(null=True, max_length=30,verbose_name='Rangi')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Mashina "
        verbose_name_plural = "Mashinalar "


class Employees(models.Model):
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    prof = models.CharField(verbose_name='Kasbi',max_length=30)
    name = models.CharField(verbose_name='Ismi', max_length=30)

    def __str__(self):
        return self.prof
    class Meta:
        verbose_name = "Ishchi "
        verbose_name_plural = "Ishchilar "
