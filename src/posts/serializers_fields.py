
























# from rest_framework.fields import Field




# class LikeCountField(Field):
#     def __init__(self, **kwargs):
#         kwargs['source'] = '*'
#         kwargs['read_only'] = True
#         super(LikeCountField, self).__init__(**kwargs)
    
#     def to_representation(self, post):
#         return post.like_count_id()


# class CommentCountField(Field):
#     def __init__(self, **kwargs):
#         kwargs['source'] = '*'
#         kwargs['read_only'] = True
#         super(CommentCountField, self).__init__(**kwargs)

#     def to_representation(self, post):
#         return post.comment_count_id()




# class CommentField(Field):
#     def __init__(self, **kwargs):
#         kwargs['source'] = '*'
#         super(CommentField, self).__init__(**kwargs)

#     def to_representation(self, comment):
#         return comment.post