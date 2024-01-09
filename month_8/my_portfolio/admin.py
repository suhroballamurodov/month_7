from django.contrib import admin
from .models import *



class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','ism', 'email', 'subyekt','xabar')
    search_fields = ['ism','email']
    ordering = ['ism', 'email']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content','updated_at','created_at']
    search_fields = ['title','content']
    ordering = ['title','content']


admin.site.register(ContactModel, ContactAdmin)
admin.site.register(Post,PostAdmin)