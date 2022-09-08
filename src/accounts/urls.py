from django.urls import path, include
from .views import UserProfileApiView


urlpatterns = [
    
    path('api/v1/<str:username>/profile', UserProfileApiView.as_view())

]



