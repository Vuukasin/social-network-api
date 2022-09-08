from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

User = get_user_model()
from .models import *

from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from api.serializers import UserOwnerSerializer


# ---------- Comments ---------- #

class CommentSerializer(serializers.ModelSerializer):
    user = UserOwnerSerializer()
    posted = serializers.DateTimeField(format='%Y-%m-%d, %H:%M')
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'posted']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'text']

# ---------- Likes ---------- #

class LikeSerializer(serializers.ModelSerializer):
    user = UserOwnerSerializer()
    class Meta:
        model = Like
        fields = ['user']


class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Like.objects.all(),
                fields=['user', 'post']
            )
        ]

# ------------ Posts ----------- #
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserOwnerSerializer(read_only=True)
    comments = serializers.SerializerMethodField('paginated_post_comments')
    liked_by_req_user = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['uuid', 'user', 'comments', 'like_count', 'comment_count', 'liked_by_req_user']



    def paginated_post_comments(self, post):
        page_size = 4
        paginator = Paginator(post.comments.all(), page_size)
        page = self.context['request'].query_params.get('page') or 1
        

        comments = paginator.page(page)
        serializer = CommentSerializer(comments, many=True)

        return serializer.data

    def get_liked_by_req_user(self, post):
        user = self.context['request'].user
        liked_by_req_user = Like.objects.filter(post=post, user=user)
        if liked_by_req_user:
            return True
        return False



class PostStreamSerializer(serializers.ModelSerializer):
    user = UserOwnerSerializer()
    liked_by_req_user = serializers.SerializerMethodField()
    

    class Meta:
        model = Post
        fields = ['content', 'user', 'uuid', 'liked_by_req_user', 'like_count', 'comment_count']

    def get_liked_by_req_user(self, post):
        user = self.context['request'].user
        liked_by_req_user = Like.objects.filter(post=post, user=user)
        if liked_by_req_user:
            return True
        return False

class PostOnlyContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content']


# -------- User Related Posts --------- #

class UserPostListSerializer(serializers.ModelSerializer):
    posts = PostOnlyContentSerializer(many=True)
    class Meta:
        model = User
        fields = ['posts']


# ----------- Notifications ------------ #

































# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from .models import Post, HashTag, Like, Comment
# from api.serializers import UserPublicSerializer
# from .serializers_fields import LikeCountField, CommentCountField

# User = get_user_model()



# class HashTagSerializer(serializers.ModelSerializer):
#     name = serializers.StringRelatedField()
#     class Meta:
#         model = HashTag
#         fields = ['name']





# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
        
        

# class CommentPublicSerializer(serializers.ModelSerializer):
#     user = UserPublicSerializer(read_only=True)
#     posted = serializers.DateTimeField(format="%Y-%m-%d, %H:%M", read_only=True)
#     class Meta:
#         model = Comment
#         fields = ['user', 'text', 'posted']




# class PostCommentSerializer(serializers.ModelSerializer):
#     comments = CommentPublicSerializer(many=True)
#     class Meta:
#         model = Post
#         fields = ['comments']

# class PostListCreateSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(
#         view_name='post-detail',
#         lookup_field='uuid'
#     )
#     class Meta:
#         model = Post
#         fields = ['user', 'content', 'url', 'description', 'uuid']
#         read_only_fields = ['user']

# class PostDetailSerializer(serializers.ModelSerializer):
#     user = UserPublicSerializer(read_only=True)
#     comments = CommentPublicSerializer(many=True, read_only=True)
#     posted = serializers.DateTimeField(format="%Y-%m-%d, %H:%M", read_only=True)
#     hashtags = HashTagSerializer(many=True)
#     # likesList_url = serializers.HyperlinkedIdentityField(
#     #     view_name='post-likes',
#     #     lookup_field='uuid'
#     # )

#     class Meta:
#         model = Post
#         fields = ['user', 'content', 'description', 'hashtags', 'like_count', 'comment_count', 'posted', 'comments']
#         extra_kwargs = {'content': {'read_only': True}}



# class PostStreamSerializer(serializers.ModelSerializer):
#     user = UserPublicSerializer(read_only=True)
#     class Meta:
#         model = Post
#         fields = ['content', 'user', 'like_count', 'comment_count']


# class LikeListSerializer(serializers.ModelSerializer):
#     user = UserPublicSerializer(read_only=True)
#     class Meta:
#         model = Like
#         fields = ['user']
# class LikeSerializer(serializers.ModelSerializer):
#     user = UserPublicSerializer(read_only=True)
#     class Meta:
#         model = Like
#         fields = ['id', 'post', 'user']



# class PostLikeSerializer(serializers.ModelSerializer):
#     likes = LikeListSerializer(many=True)
#     class Meta:
#         model = Post
#         fields = ['likes']












