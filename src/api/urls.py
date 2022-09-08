from django.urls import path, include
from .views import RegisterApi, LoginApi, UserApi
from knox.views import LogoutView



urlpatterns = [
    path('api/v1/auth', include('knox.urls')),
    path('api/v1/auth/register', RegisterApi.as_view()),
    path('api/v1/auth/login', LoginApi.as_view()),
    path('api/v1/auth/user', UserApi.as_view()),
    path('api/v1/auth/logout', LogoutView.as_view(), name='knox_logout')
]