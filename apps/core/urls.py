from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',

    url(r'todo-apps$', views.ListCreateTodoApp.as_view(), name='list-create-todo-app'),

)
