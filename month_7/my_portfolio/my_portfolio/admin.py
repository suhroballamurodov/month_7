from django.contrib import admin
from .models import *



class ContactAdmin(admin.ModelAdmin):
    list_display = ('ism', 'email', 'subyekt','xabar')
    search_fields = ['ism','email']
    ordering = ['ism', 'email']



admin.site.register(ContactModel, ContactAdmin)