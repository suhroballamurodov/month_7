from django.contrib import admin
from .models import *


class MatheAdmin(admin.ModelAdmin):
    list_display = ('id','birinchi_son','ikkinchi_son','natija')
    search_fields = ['natija']
    ordering = ['natija']



class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'savol', 'a', 'b','c','rasm')
    search_fields = ['savol']
    ordering = ['savol']



admin.site.register(MatheModel, MatheAdmin)
admin.site.register(TestModel, TestAdmin)