from django.urls import path
from .views import TodoListCreateView, TodoRetrieveUpdateDeleteView

urlpatterns = [
    path("", TodoListCreateView.as_view()),
    path("<int:id>/", TodoRetrieveUpdateDeleteView.as_view()),
]
