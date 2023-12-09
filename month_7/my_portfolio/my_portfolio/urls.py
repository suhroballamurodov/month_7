from django.urls import path
from .views import *
from . import views
from django.urls import path

urlpatterns = [
    path('', main, name='main'),
    path('portfolio_details/', portfolio_details, name='portfolio_details'),
    # path('sendmail/', sendmail),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]