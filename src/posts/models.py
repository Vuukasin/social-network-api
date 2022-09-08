from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete, post_save
from django.db.models import Q

import uuid

User = get_user_model()
from notifications.models import Notification

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class HashTag(models.Model):
    name = models.CharField(max_length=25, blank=False, unique=True)

    def __str__(self):
        return f'#{self.name}'




class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.FileField(upload_to=user_directory_path)
    description = models.TextField(max_length=255, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    hashtags = models.ManyToManyField(HashTag, blank=True)


    def __str__(self):
        return f"{self.user.username}'s post"

    # def comment_count_id(self):
    #     return Comment.count_comments_for_post_with_id(self.id)

    # def like_count_id(self):
    #     return Like.count_likes_for_post_with_id(self.id)

    def comment_count(self):
        return self.comments.count()

    def like_count(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, blank=False, null=False)
    posted = models.DateTimeField(auto_now_add=True)
    notify_code = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.user.username}'s comment"

    # @classmethod
    # def count_comments_for_post_with_id(cls, post_id):
    #     count_query = Q(post_id=post_id)
    #     return cls.objects.filter(count_query).count()

    def comment_notification(sender, instance, *args, **kwargs):
        comment = instance
        post = comment.post
        sender = comment.user
        notify = Notification(post=post, sender=sender, user=post.user, code=comment.notify_code, notification_type=2)
        notify.save()

    def comment_delete_notification(sender, instance, *args, **kwargs):
        comment = instance
        post = comment.post
        sender = comment.user
        notify = Notification.objects.filter(post=post, user=post.user, sender=sender, notification_type=2, code=comment.notify_code)
        notify.delete()

post_save.connect(Comment.comment_notification, sender=Comment)
post_delete.connect(Comment.comment_delete_notification, sender=Comment)


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    notify_code = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.follower} -> {self.following}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'following'], name='unique_follow')
        ]


    def follow_notification(sender, instance, *args, **kwargs):
        follow = instance
        sender = follow.follower
        following = follow.following
        notify = Notification(sender=sender, user=following, notification_type=3, code=follow.notify_code)
        notify.save()

    def unfollow_notification(sender, instance, *args, **kwargs):
        follow = instance
        sender = follow.follower
        following = follow.following
        notify = Notification.objects.filter(sender=sender, user=following, notification_type=3, code=follow.notify_code)
        notify.delete()

post_save.connect(Follow.follow_notification, sender=Follow)
post_delete.connect(Follow.unfollow_notification, sender=Follow)
        




class Stream(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='stream_following', null=True)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_following')
    date = models.DateTimeField(auto_now_add=True)


    def add_post(sender, instance, created, *args, **kwargs):
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)
        for follower in followers:
            stream = Stream(post=post, user=follower.follower, date=post.posted, following=user)
            stream.save()

    def add_following(sender, instance, created, *args, **kwargs):
        posts = Post.objects.all().filter(user=instance.following)
        if created:
            for post in posts:
                Stream.objects.create(post=post, following=instance.following, user=instance.follower)

post_save.connect(Stream.add_post, sender=Post)
post_save.connect(Stream.add_following, sender=Follow)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notify_code = models.UUIDField(default=uuid.uuid4, editable=False)

    # @classmethod
    # def count_like_for_post_with_id(cls, post_id):
    #     count_query = Q(post_id=post_id)
    #     return cls.objects.filter(count_query).count()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='unique_like')
        ]

    def like_notification(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.user
        notify = Notification(sender=sender, post=post, user=post.user, notification_type=1, code=like.notify_code)
        notify.save()

    def unlike_notification(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.user
        notify = Notification.objects.filter(post=post, sender=sender, notification_type=1, code=like.notify_code)
        notify.delete()


post_save.connect(Like.like_notification, sender=Like)
post_delete.connect(Like.unlike_notification, sender=Like)


# class Story(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_owner')
#     content = models.FileField(upload_to=user_directory_path)
#     posted = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = "stories"
    

# class StoriesStream(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_following')
#     story = models.ForeignKey(Story, on_delete=models.CASCADE)

#     def add_following(sender, instance, created, *args, **kwrgs):
#         stories = Story.objects.all().filter(user=instance.following)
#         if created:
#             for story in stories:
#                 StoriesStream.objects.create(following=instance.follwing, user=instance.follower, story=story, date=story.posted)


#     def add_stoy(sender, instance, *args, **kwargs):
#         new_story = instance
#         user = new_story.user
#         followers = Follow.objects.all().filter(following=user)
#         for follower in followers:
#             storystream = StoriesStream(story=new_story, user=follower.follower, date=new_story.posted, following=user)
#             storystream.save()

# post_save.connect(StoriesStream.add_following, sender=Follow)
# post_save.connect(StoriesStream.add_stoy, sender=Story)








