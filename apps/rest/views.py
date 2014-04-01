from rest_framework import generics

from apps.core import models

from . import serializers


class ListCreateTodoApp(generics.ListCreateAPIView):
    model = models.TodoApp
    serializer_class = serializers.TodoAppSerializer


class RetrieveUpdateDestroyTodoApp(generics.RetrieveUpdateDestroyAPIView):
    model = models.TodoApp
    serializer_class = serializers.TodoAppSerializer
