from django.urls import path
from . import views
from .views import *
# from django.views.generic import ListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('create', PostCreateView.as_view(), name='create_post'),
    path('post/<str:pk>', PostDetailView.as_view(), name='post'),
    path('postdelete/<str:pk>',PostDeleteView.as_view(), name='postdelete'),
    path('postupdate/<str:pk>', PostUpdateView.as_view(), name='postupdate'),
]




    # path('posts/', views.posts, name='posts'),
    # path('post/<str:pk>', views.post, name="post"),
    # path('postdelete/<str:pk>', views.postdelete, name='postdelete'),
    # path('postupdate/<str:pk>', views.updatepost, name='postupdate'),
    # # path('postcreate/', Create.as_views(), name='create'),
    # path('posts/create/', views.create_post, name = 'create_post'),