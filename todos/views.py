from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer
from accounts.permissions import IsPaidUser  # from Part 3

# class TodoListCreateView(generics.ListCreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated, IsPaidUser]

#     def get_queryset(self):
#         if self.request.user.is_active:
#             return Todo.objects.all()
#         return Todo.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class TodoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated, IsPaidUser]
#     lookup_field = "id"

#     def get_queryset(self):
#         return Todo.objects.filter(user=self.request.user)

# FINAL WAY 

# todos/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer
from accounts.permissions import IsAdminOrPaidUser

from django_filters.rest_framework import DjangoFilterBackend #FOR filtered part

class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsAdminOrPaidUser]

    ##2nd search For Filtering 
    # search_fields = ["title"]  # 🔥 allow search by title
    # filter_backends = [filters.SearchFilter]  # enable search only

    # # 3rd part fitering
    # filter_backends = [DjangoFilterBackend]     # 🔥 enable filtering
    # filterset_fields = ["completed"]           # 🔥 filter field

    ## 4th ordering 
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at", "title"]   # fields allowed for sorting

    def get_queryset(self):
        user = self.request.user
        # Admin sees all todos
        if user.is_staff:
            return Todo.objects.all()
        # Normal user sees only their own todos
        return Todo.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsAdminOrPaidUser]
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Todo.objects.all()
        return Todo.objects.filter(user=user)
