from rest_framework.fields import Field



class PostsCountField(Field):
    def __init__(self, **kwargs):
        kwargs['source'] = '*'
        kwargs['read_only'] = True
        super(PostsCountField, self).__init__(**kwargs)

    def to_representation(self, user):
        return user.profile.posts_count()

class FollowingCountField(Field):
    def __init__(self, **kwargs):
        kwargs['source'] = '*'
        kwargs['read_only'] = True
        super(FollowingCountField, self).__init__(**kwargs)

    def to_representation(self, user):
        return user.profile.following_count()

class FollowersCountField(Field):
    def __init__(self, **kwargs):
        kwargs['source'] = '*'
        kwargs['read_only'] = True
        super(FollowersCountField, self).__init__(**kwargs)
    def to_representation(self, user):
        return user.profile.followers_count()