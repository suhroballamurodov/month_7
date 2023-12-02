from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', html, name='html'),
    path('base/', base, name='base'),
    path('page1/', page1, name='page1'),
    path('page2/', page2, name='page2'),
    path('page3/', page3, name='page3'),
    path('page4/', page4, name='page4'),
    path('page5/', page5, name='page5'),
    path('page6/', page6, name='page6'),
]