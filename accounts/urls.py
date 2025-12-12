from django.urls import path
from .views import (
    RegisterAPIView,
    LoginAPIView,
    RefreshTokenAPIView,
    VerifyTokenAPIView,
    LogoutAPIView,
    ProfileAPIView,
    UpgradeAPIView,
    AdminUserListAPIView
)

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", LoginAPIView.as_view()),
    path("refresh/", RefreshTokenAPIView.as_view()),
    path("verify/", VerifyTokenAPIView.as_view()),
    #Part 2
    path("logout/", LogoutAPIView.as_view()),
    path("profile/", ProfileAPIView.as_view()),
    path("upgrade/", UpgradeAPIView.as_view()),

    #Part 3
    path("users/", AdminUserListAPIView.as_view())
]
