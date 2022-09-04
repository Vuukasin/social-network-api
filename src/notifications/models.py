from random import choices
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()





class Notification(models.Model):

    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'Follow'))

    code = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_to')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_from')
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, blank=True, null=True, related_name='post_notificatino')
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
