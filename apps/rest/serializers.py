from rest_framework import serializers


from apps.core import models


class TodoAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TodoApp
