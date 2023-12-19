from django.urls import path

from .views import *

urlpatterns = [
    path('profile/', profile_view, name="profile"),
    path('register/', RegisterView.as_view(), name="register"),
    # path('register/passwords/', RegisterViewPasswords.as_view(), name="register_passwords"),
]
