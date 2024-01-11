from django.contrib import admin
from .models import *


class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand_locations']
    search_fields = ['name']
    ordering = ['name']


class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','color']
    search_fields = ['name', 'price','color']
    ordering = ['name', 'price']



class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['prof', 'name']
    search_fields = ['name','prof']
    ordering = ['name', 'prof']


admin.site.register(Brand, BranchAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Employees, EmployeesAdmin)