from django.urls import path, include
from .views import UserProfileApiView


urlpatterns = [
    path('api/<str:username>/', UserProfileApiView.as_view())
    
]



