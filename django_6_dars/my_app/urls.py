from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', blogsayt),
    path('news/', yangilik),
]