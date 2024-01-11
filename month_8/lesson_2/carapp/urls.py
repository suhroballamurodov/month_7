from django.urls import path
from .views import *

urlpatterns = [
    path('brands', BrandListAPIView.as_view(), name='brand-list'), #brandni qaytaruvchi API
    path('brands/<int:brand_id>/employees', EmployeeListAPIView.as_view(), name='employee-list'), #brandda ishlovchi ishchilarni ismi va kasbini qaytaruvchi API
    path('brands/<int:brand_id>/cars', CarListAPIView.as_view(), name='car-list'), #branddagi mashinalarni qaytaruvchi API
    path('brands/<int:brand_id>/car_count/', CarCountAPIView.as_view(), name='car-count'), #branddagi mashinalar sonini qaytaruvchi API
    path('',car), #Web application ishlayotganligi bilish uchun 
]
