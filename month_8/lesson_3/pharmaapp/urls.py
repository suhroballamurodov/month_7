from django.urls import path
from .views import *


urlpatterns = [
    path('', pharma, name='pharma'), #sayt ishlashini tekshirish uchun manzil
    path('customers/', CustomerListAPIView.as_view(), name='customer-list'), #customerlarni qaytaruvchi API
    path('customers/<int:customer_id>/purchasing', CustomerPurchasingListAPIView.as_view()), #Customerning barcha sotib olgan dorilarini qaytaruvchi API
    path('customers/<int:med_id>/med',PurchasingListAPIView.as_view()), #Ayni bir dorini sotib olgan customerlarni qaytaruvchi API
    path('customers/<int:med_id>/time',TimeListAPIView.as_view()), #00 - 23 gacha sotilgan dorilar ro'yxxatini qaytaruvchi API
]