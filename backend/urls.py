# -*- coding: utf-8 -*-
from django.urls import path
from .views import ListPost, DetailPost, CreatePost

urlpatterns =[
    path('create-post/', CreatePost.as_view(), name='create-post'),
    path('posts/<int:pk>/', DetailPost.as_view(), name='post-detail'),
    path('posts/', ListPost.as_view(), name='post-list'),
]
