from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile
from posts.models import Follow
from posts.serializers import PostProfileSerializer
User = get_user_model()



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location']



class UserProfileSerialzier(serializers.ModelSerializer):
    profile = ProfileSerializer()
    posts = PostProfileSerializer(many=True)

    

    def get_following_count(self, user_obj):
        following_count = Follow.objects.filter(follower=user_obj).count()
        return following_count

    def get_followers_count(self, user_obj):
        followers_count = Follow.objects.filter(following=user_obj).count()
        return followers_count

    
    class Meta:
        model = User
        fields = ['username', 'profile', 'first_name', 'last_name', 'posts']
        
