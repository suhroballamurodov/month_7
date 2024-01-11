from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', main, name='main'),
    path('portfolio_details/', portfolio_details, name='portfolio_details'),
    path('api/', include(router.urls)),  #API uchun link
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('posts', views.getData),
] 