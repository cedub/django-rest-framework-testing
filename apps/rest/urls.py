from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',

    url(r'todo-apps$', views.ListCreateTodoApp.as_view(), name='list-create-todo-app'),
    url(r'todo-apps/(?P<pk>\d+)$', views.RetrieveUpdateDestroyTodoApp.as_view(), name='udpate-destroy-todo-app'),

)
