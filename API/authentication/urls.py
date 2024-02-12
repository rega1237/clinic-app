from django.urls import path
from .views import UserRegistrationView, LogOutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-registration"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
