from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location', 'posts_count', 'following_count', 'followers_count']


class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileInfoSerializer()
    class Meta:
        model = User
        fields = ['username', 'profile']



