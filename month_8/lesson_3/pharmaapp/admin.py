from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','name','l_name','contact_add']
    search_fields = ['name','l_name','contact_add']
    ordering = ['name']

class PharmacistAdmin(admin.ModelAdmin):
    list_display = ['id','name','l_name','contact_add']
    search_fields = ['name','l_name','contact_add']
    ordering = ['name']


class MedicinesAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','price','med_category']
    search_fields = ['name','price','med_category']
    ordering = ['name']


class PurchasingAdmin(admin.ModelAdmin):
    list_display = ['id','customer_id','med_id','amount','date']
    search_fields = ['customer_id','amount','data']
    ordering = ['customer_id']


class SalesAdmin(admin.ModelAdmin):
    list_display = ['id','pharm_id','customer_id','med_id','count','purchase_id','date','total_amount']
    search_fields = ['customer_id','amount','date']
    ordering = ['customer_id']


class ReportsAdmin(admin.ModelAdmin):
    list_display = ['id','sales_id','customer_id','purchase_id','date']
    search_fields = ['customer_id','sales_id','date']
    ordering = ['customer_id']


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Pharmacist,PharmacistAdmin)
admin.site.register(Medicines,MedicinesAdmin)
admin.site.register(Purchasing,PurchasingAdmin)
admin.site.register(Sales,SalesAdmin)
admin.site.register(Reports,ReportsAdmin)