from django.db import models
# from django.contrib.auth.models import User



class Botinfo(models.Model):
    send_time = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")
    info = models.TextField(verbose_name="Botga yozilgan ma'lumotlar")
    email_pochta = models.EmailField()

    def __str__(self):
        return self.email_pochta
    
    class Meta:
        verbose_name = 'Bot info'
        verbose_name_plural = 'Bot infos'