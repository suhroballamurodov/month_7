from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('lesson9/', lesson_9)
]