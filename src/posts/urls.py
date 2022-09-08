from django.urls import path
from .views import (
    PostCreateApiView, PostDetailApiView, UserPostListApiView, PostStreamListApiView,
    
    CommentCreateApiView, ManageCommentView,

    LikeCreateApiView, LikeDestroyApiView,
    
     )

urlpatterns = [
    path('api/v1/posts/', PostCreateApiView.as_view()),
    path('api/v1/posts/<uuid:uuid>/', PostDetailApiView.as_view(), name='post-detail'),
    path('api/v1/stream/', PostStreamListApiView.as_view()),

    path('api/v1/likes/', LikeCreateApiView.as_view()),
    path('api/v1/likes/<int:pk>/', LikeDestroyApiView.as_view()),

    path('api/v1/comments/<int:comment_id>/', ManageCommentView.as_view()),
    path('api/v1/comments/', CommentCreateApiView.as_view()),

    path('api/v1/<str:username>/posts', UserPostListApiView.as_view()),


    

























    # -------- POSTS ---------- #
    # path('api/v1/posts/', PostCreateApiView.as_view(), name='posts'), # //

    # path('api/v1/posts/<uuid:uuid>/', PostDetailApiView.as_view(), name='post-detail'), # //

    # path('api/v1/posts/<username:username>'),

    # path('api/v1/posts/<uuid:uuid>/comments', PostCommentListApiView.as_view()),

    # path('api/v1/posts/<uuid:uuid>/likes', PostLikeListApiView.as_view(), name='post-likes'), # //

    # path('api/v1/posts/stream', PostStreamApiView.as_view()),


    # ------- COMMENTS --------  #
    # path('api/v1/comments/', CommentCreateApiView.as_view()),
    # path('api/v1/comments/<int:pk>', CommentDestroyApiView.as_view()),
    # ------- LIKES -------- #

    # path('api/v1/likes/', LikeCreateApiView.as_view()),
    # path('api/v1/likes/<int:pk>', LikeDestroyApiView.as_view())


    # ------- HASHTAGS --------- #
    
    # ------- FOLLOWS ---------- #

    # ------- NOTIFICATIONS -------- #
    

]
