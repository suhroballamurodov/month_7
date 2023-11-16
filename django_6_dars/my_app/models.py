from django.db import models
from django.conf import Settings

# Create your models here.

def default_photos():
    return 'default.jpg'

class YangilikModel(models.Model):
    title = models.CharField(max_length=50, blank=True, default='Mavzusi nomalum xabar')
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photos = models.ImageField(upload_to=default_photos,default='default.jpg')
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'