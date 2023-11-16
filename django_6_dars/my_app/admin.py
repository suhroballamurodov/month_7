from django.contrib import admin

# Register your models here.

from .models import YangilikModel
from .views import YangilikModel

class YangilikAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created','updated','photos','published' )
    search_fields = ('title','created')

admin.site.register(YangilikModel, YangilikAdmin)