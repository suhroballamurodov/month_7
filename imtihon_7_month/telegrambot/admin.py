from django.contrib import admin
from .models import *



class BotAdmin(admin.ModelAdmin):
    list_display = ['send_time','email_pochta']
    ordering = ['send_time']
    search_fields = ['email_pochta', 'send_time']



admin.site.register(Botinfo,BotAdmin)