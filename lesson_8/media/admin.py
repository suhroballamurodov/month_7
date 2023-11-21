from django.contrib import admin
from .models import *


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id','icon','content')
    search_fields = ['content']


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','owner','text','image')
    search_fields = ['owner', 'text']
    

class MediaAdmin(admin.ModelAdmin):
    list_display = ('id','last_name','first_name','image','work','testiomonial')
    search_fields = ['last_name', 'first_name']


class RasmlarAdmin(admin.ModelAdmin):
    list_display = ('rasm',)
    search_fields = ['rasm',]


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','subject','email','message')
    search_fields = ['name', 'email']

class AboutmeAdmin(admin.ModelAdmin):
    list_display = ('name', 'about','my_app','my_persent')
    search_fields = ['name', 'my_app']


admin.site.register(Post, PostAdmin)
admin.site.register(MediaUser, MediaAdmin)
admin.site.register(Lesson_9, LessonAdmin)
admin.site.register(Rasmlar, RasmlarAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Aboutme, AboutmeAdmin)