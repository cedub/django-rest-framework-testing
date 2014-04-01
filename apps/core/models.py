from django.db import models


class TodoApp(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    description = models.TextField()