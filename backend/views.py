from django.shortcuts import render, redirect
from django.urls import reverse

from rest_framework import generics
from .models import Post
from api.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated


class ListPost(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print('Body')
        # serializer.save(user=self.request.user)
        serializer.save()

        post_list_url = reverse('post-list')
        return redirect(post_list_url)


def show_page(request):
    return render(request, 'mypage.html')