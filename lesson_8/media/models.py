from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


class MediaUser(models.Model):
    def image_tag(self,obj):
        return format_html("<img src='mediafiles'>",{obj.image})
    image_tag.short_description = 'Image'
    last_name = models.CharField(max_length=30,verbose_name='Ismi')
    first_name = models.CharField(max_length=30, verbose_name='Familiyasi')
    work = models.CharField(max_length=50,verbose_name='Kasbi')
    testiomonial = models.TextField(default='Bu dizayner haqida yaxshi fikrdaman', verbose_name='Sharh')
    image = models.ImageField(null=True, blank=True, verbose_name='Rasmi')

    def __str__(self):
        return self.last_name
    
    class Meta:
        verbose_name = 'MediaUser'
        verbose_name_plural = 'MediaUsers'


class Post(models.Model):
    owner = models.ForeignKey(MediaUser, null=True, on_delete=models.CASCADE,verbose_name= 'Yaratuvchi')
    image = models.ImageField(null=True, blank=True, verbose_name='Rasmi')
    photo = models.ImageField(null=True, blank=True, verbose_name='Rasmi_1')
    text = models.TextField(verbose_name='Matn')

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'


class Lesson_9(models.Model):
    icon = models.ImageField(null=True, blank=True, verbose_name='Iconka')
    content = models.TextField(blank=True, default="Bu haqida to'liq ma'lumot topa olmadik",verbose_name='Matn')

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Rasmlar(models.Model):
    rasm = models.ImageField(null=True, blank=False, verbose_name='Rasm')

    # def __str__(self):
    #     return self.rasm
    
    class Meta:
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'


class Contact(models.Model):
    name = models.TextField(blank=False, verbose_name='Ism')
    subject = models.TextField(blank=False, verbose_name='Subject')
    email = models.EmailField(blank=False, verbose_name='Email manzil')
    message = models.TextField(blank=True, verbose_name='Xabar')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Aboutme(models.Model):
    name = models.TextField(blank=False, verbose_name='Ism')
    about = models.TextField(blank=False,default='Men Grafik dizaynerman',verbose_name='Men haqimda qisqacha')
    my_app = models.TextField(blank=True, verbose_name='Men ishlaydigan dasturlar')
    my_persent = models.CharField(blank=False, default=50, verbose_name='Qay darajada bilishim')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Aboutour'