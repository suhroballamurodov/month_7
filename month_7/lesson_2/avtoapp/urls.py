from . import views
from django.urls import path

urlpatterns = [    
    path('avto-list', views.avtoList, name='avto-list'),
    path('avto-create', views.avtoCreate, name='avto-create'),
    path('avto-update/<int:id>', views.avtoUpdate, name='avto-update'),
    path('avto-delete/<int:id>', views.avtoDelete, name='avto-delete'),
]