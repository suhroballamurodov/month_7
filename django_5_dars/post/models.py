from django.db import models

# Create your models here.

class Blogpost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Sarlavha')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")
    photos = models.ImageField(upload_to='photos/%Y/%m/%d',default='rasm mavjud emas', verbose_name="Rasmi")


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Veb sayt sahifa"
        verbose_name_plural = "Veb sayt sahifalari"
        ordering = ['created_at', 'content']