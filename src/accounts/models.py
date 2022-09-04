from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


User = get_user_model()
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to=user_directory_path, default='avatar.png')
    bio = models.TextField(max_length=255, blank=True)
    location = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def create_profile(sender, instance, created, *args, **kwargs):
        if created:
            Profile.objects.create(user=instance)



post_save.connect(Profile.create_profile, sender=User)





