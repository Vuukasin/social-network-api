from rest_framework import serializers
from .models import Notification



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['sender', 'notification_type', 'is_seen', 'date']



