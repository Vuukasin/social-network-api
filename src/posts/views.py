from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Post, Stream, Comment
from .serializers import PostDetailSerializer, PostCreateSerializer, PostListSerializer, CommentCreateSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from api.mixins import UserQuerySetMixin
from rest_framework.response import Response
from rest_framework import status
from django.db.models.signals import pre_save

class PostListApiView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class PostCreateApiView(CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    queryset = Post.objects.all()
    lookup_field = 'uuid'



class CommentCreateApiView(CreateAPIView):
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

# class PostDetailApiView(RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
#     queryset = Post.objects.all()
#     lookup_field = 'uuid'


    

# class PostStreamListApiView(ListAPIView):
#     serializer_class = PostStreamSerializer

#     def get_queryset(self):
#         user = self.request.user
#         posts = Stream.objects.filter(user=user)
#         post_ids = []
#         for post in posts:
#             post_ids.append(post.post.id)
#         qs = Post.objects.all().filter(id__in=post_ids).order_by('posted')
#         return qs



