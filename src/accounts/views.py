from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from api.permissions import IsOwnerOrReadOnly
from .serializers import UserProfileSerializer

User = get_user_model()


class UserProfileApiView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
