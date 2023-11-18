from django.contrib import admin
from .models import Post, Lesson_9, MediaUser


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id','icon','content')
    search_fields = ['content']


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','owner','text','image')
    search_fields = ['owner', 'text']


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id','last_name','first_name','image')
    search_fields = ['last_name', 'first_name']


admin.site.register(Post, PostAdmin)
admin.site.register(MediaUser, MediaAdmin)
admin.site.register(Lesson_9, LessonAdmin)