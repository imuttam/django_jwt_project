from django.urls import path
from .views import (
    SiteListCreateAPIView,
    SiteRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path("sites/", SiteListCreateAPIView.as_view(), name="site-list-create"),
    path("sites/<int:pk>/", SiteRetrieveUpdateDestroyAPIView.as_view(), name="site-detail"),
]
