from django.urls import path, include
from .views import *

urlpatterns = [
    path('', math),
    path('test/', test, name='test')
]