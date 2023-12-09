from django.db import models


class ContactModel(models.Model):
    ism = models.CharField(null=True, blank=False, max_length=30, verbose_name='Ism')
    email = models.EmailField(null=True, blank=False,verbose_name='Email')
    subyekt = models.TextField(null=True, blank=True,verbose_name='Subyekt')
    xabar = models.TextField(null=True, blank=False, verbose_name='Xabar')

    def __str__(self):
        return self.ism
    
    class Meta:
        verbose_name = "Kontakt ma'lumoti"
        verbose_name_plural = "Kontakt ma'lumotlari"
        