from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, HashTag, Like, Comment
from api.serializers import UserPublicSerializer

User = get_user_model()

########### HASHTAGS SERIALIZERS ###########

class HashTagSerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField()
    class Meta:
        model = HashTag
        fields = ['title']



########## COMMENTS SERIALIZERS ##########

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']

class CommentPublicSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer()
    avatar = serializers.ImageField(source='user.profile.avatar')
    class Meta:
        model = Comment
        fields = ['user', 'avatar', 'text', 'posted']

########## POSTS SERIALIZERS ###########

class PostListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post-detail',
        lookup_field='uuid'
    )
    class Meta:
        model = Post
        fields = ['user', 'content', 'url']


class PostProfileSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post-detail',
        lookup_field='uuid'
    )
    class Meta:
        model = Post
        fields = ['content', 'url']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content', 'description', 'hashtags']


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    avatar = serializers.ImageField(source='user.profile.avatar', read_only=True)
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    comments = CommentPublicSerializer(many=True)
    

    class Meta:
        model = Post
        fields = ['user', 'content', 'avatar', 'description', 'like_count', 'comment_count', 'posted', 'comments']
        extra_kwargs = {'content': {'read_only': True}}

    def get_comments(self, post_obj):
        comments = Comment.objects.filter(post=post_obj)
        return comments

    def get_like_count(self, post_obj):
        like_count = Like.objects.filter(post=post_obj).count()
        return like_count
    
    def get_comment_count(self, post_obj):
        comment_count = Comment.objects.filter(post=post_obj).count()
        return comment_count










######## COMMENTS SERIALIZERS ########








# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'


# class PostStreamSerializer(serializers.ModelSerializer):
#     user = UserPublicSerializer(read_only=True)
#     avatar = serializers.ImageField(source='user.profile.avatar')
#     like_count = serializers.SerializerMethodField('_get_like_count')
#     comment_count = serializers.SerializerMethodField('_get_comment_count')

#     def _get_like_count(self, post_obj):
#         like_count = Like.objects.all().filter(post=post_obj).count()
#         return like_count
#     def _get_comment_count(self, post_obj):
#         comment_count = Comment.objects.all().filter(post=post_obj).count()
#         return comment_count


#     class Meta:
#         model = Post
#         fields = ['content', 'user', 'avatar', 'like_count', 'comment_count']



