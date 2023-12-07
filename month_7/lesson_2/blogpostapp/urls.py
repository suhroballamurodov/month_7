from django.urls import path
from . import views
from .views import *
from django.views.generic import ListView

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('post/<str:pk>', views.post, name="post"),
    path('postdelete/<str:pk>', views.postdelete, name='postdelete'),
    path('postupdate/<str:pk>', views.updatepost, name='postupdate'),
    # path('postcreate/', Create.as_views(), name='create'),
    path('posts/create/', views.create_post, name = 'create_post'),
]