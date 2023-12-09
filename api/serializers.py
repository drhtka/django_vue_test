# -*- coding: utf-8 -*-
from rest_framework import serializers
from backend.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created_at')
