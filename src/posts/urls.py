from django.urls import path
from .views import PostCreateApiView, PostListApiView, PostDetailApiView

urlpatterns = [

    path('api/post/', PostListApiView.as_view()),
    path('api/post-create/', PostCreateApiView.as_view()),
    # path('api/post-stream/', PostStreamListApiView.as_view()),
    path('api/post/<uuid:uuid>/', PostDetailApiView.as_view(), name='post-detail')

]
