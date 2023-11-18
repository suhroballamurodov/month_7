from django.db import models
from django.contrib.auth.models import User

class MediaUser(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.last_name



class Post(models.Model):
    owner = models.ForeignKey(MediaUser, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField()

    def __str__(self) -> str:
        return self.text
    


class Lesson_9(models.Model):
    icon = models.ImageField(null=True, blank=True)
    content = models.TextField(blank=True, default="Bu haqida to'liq ma'lumot topa olmadik")

    def __str__(self):
        return self.content