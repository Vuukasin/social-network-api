from django.contrib import admin
from .models import HashTag, Post, Follow, Stream, Comment, Like

admin.site.register(HashTag)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Stream)
admin.site.register(Comment)
admin.site.register(Like)