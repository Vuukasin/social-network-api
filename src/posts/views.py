from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, ListCreateAPIView
from .models import *
from api.permissions import IsOwnerOrReadOnly


from rest_framework import permissions
from api.mixins import UserQuerySetMixin
from .permissions import IsOwnerOrPostOwnerOrReadOnly
from .serializers import (

    PostSerializer, PostDetailSerializer, UserPostListSerializer, PostStreamSerializer,

    CommentSerializer, CommentCreateSerializer,

    LikeSerializer, LikeCreateSerializer

    

    )



# ------------ Posts ----------- #
class PostCreateApiView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'uuid'




class PostStreamListApiView(ListAPIView):
    serializer_class = PostStreamSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        posts = Stream.objects.filter(user=user)
        post_ids = []
        for post in posts:
            post_ids.append(post.post.id)
        qs = Post.objects.filter(id__in=post_ids).order_by('-posted')
        return qs


# class PostStreamApiView(ListAPIView):
#     serializer_class =PostStreamSerializer
#     def get_queryset(self):
#         user = self.request.user
#         posts = Stream.objects.filter(user=user)
#         post_ids = []
#         for post in posts:
#             post_ids.append(post.post.id)
#         qs = Post.objects.filter(id__in=post_ids).order_by('posted')
#         return qs


# ---------- Post User Related Views ---------- #
class UserPostListApiView(RetrieveAPIView):
    serializer_class = UserPostListSerializer
    queryset = User.objects.all()
    lookup_field = 'username'


# ---------- Comments ---------- #

class CommentCreateApiView(CreateAPIView):
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)



class ManageCommentView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    permission_classes = [IsOwnerOrPostOwnerOrReadOnly]
    queryset = Comment.objects.all()



# ---------- Likes ---------- #


class LikeCreateApiView(CreateAPIView):
    serializer_class = LikeCreateSerializer
    queryset = Like.objects.all()
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class LikeDestroyApiView(DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    lookup_field = 'pk'
    
    

# --------- Notifications ------------ #







































# from django.shortcuts import render
# from rest_framework.generics import DestroyAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
# from .models import Post, Stream, Comment, Like

# from .serializers import (
#     PostDetailSerializer,
#     PostStreamSerializer,
#     PostCommentSerializer,
#     PostLikeSerializer,
#     PostSerializer,

#     CommentPublicSerializer,
#     CommentSerializer,
    
#     LikeSerializer,
#     )

# from api.permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import mixins
# from api.mixins import UserQuerySetMixin
# from rest_framework.response import Response
# from rest_framework import status



# class PostCreateApiView(CreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     permission_classes = [IsAuthenticated]
#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user=user)


# class PostDetailApiView(RetrieveUpdateDestroyAPIView):
#     serializer_class = PostDetailSerializer
#     permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
#     queryset = Post.objects.all()
#     lookup_field = 'uuid'


# class PostCommentListApiView(RetrieveAPIView):
#     serializer_class = PostCommentSerializer
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     lookup_field = 'uuid'




# class PostStreamApiView(ListAPIView):
#     serializer_class =PostStreamSerializer
#     def get_queryset(self):
#         user = self.request.user
#         posts = Stream.objects.filter(user=user)
#         post_ids = []
#         for post in posts:
#             post_ids.append(post.post.id)
#         qs = Post.objects.filter(id__in=post_ids).order_by('posted')
#         return qs



# class PostLikeListApiView(ListAPIView):
#     serializer_class = PostLikeSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'uuid'
#     queryset = Post.objects.all()




# ########### COMMENTS VIEWS ################



# class CommentCreateApiView(CreateAPIView):
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()
#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user=user)



# class CommentDetailApiView(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()





# class LikeCreateApiView(CreateAPIView):
#     serializer_class = LikeSerializer
#     permission_classes = [IsAuthenticated]
#     queryset = Like.objects.all()
#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user=user)


# class LikeDestroyApiView(DestroyAPIView):
#     serializer_class = LikeSerializer
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
#     queryset = Like.objects.all()
#     lookup_field = 'pk'










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



