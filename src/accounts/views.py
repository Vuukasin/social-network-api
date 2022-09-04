from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from .serializers import UserProfileSerialzier
User = get_user_model()




class UserProfileApiView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerialzier
    queryset = User.objects.all()
    lookup_field = 'username'
