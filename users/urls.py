from django.urls import path
from .views import UserProfileListAPIView

urlpatterns = [
    path('users/', UserProfileListAPIView.as_view()),
]
