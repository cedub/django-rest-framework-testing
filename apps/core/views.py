from rest_framework import generics

from apps.core import models


class ListCreateTodoApp(generics.ListCreateAPIView):
    model = models.TodoApp