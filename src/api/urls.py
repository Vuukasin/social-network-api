from django.urls import path, include
from .views import RegisterApi, LoginApi, UserApi
from knox.views import LogoutView



urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterApi.as_view()),
    path('api/auth/login', LoginApi.as_view()),
    path('api/auth/user', UserApi.as_view()),
    path('api/auth/logout', LogoutView.as_view(), name='knox_logout')
]