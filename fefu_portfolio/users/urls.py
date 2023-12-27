from django.urls import path

from .views import *
from .api_views import UserInfoAPIView

urlpatterns = [
    path('profile/', profile_view, name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
    # path('register/passwords/', RegisterViewPasswords.as_view(), name="register_passwords"),
    path('user_info/', UserInfoAPIView.as_view(), name="user_infos"),
]
