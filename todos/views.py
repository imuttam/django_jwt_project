from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer
from accounts.permissions import IsPaidUser  # from Part 3

class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsPaidUser]

    def get_queryset(self):
        if self.request.user.is_active:
            return Todo.objects.all()
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsPaidUser]
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
