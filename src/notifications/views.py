from django.shortcuts import render
from .serializer import NotificationSerializer
from .models import Notification
# Create your views here.


from rest_framework.generics import ListAPIView



class NotificationListForUser(ListAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    