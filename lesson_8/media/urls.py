from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('lesson9/', lesson_9),
    path('media/', mediauser),
    path('lesson10/', lesson10),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('images/',images, name='images'),
]