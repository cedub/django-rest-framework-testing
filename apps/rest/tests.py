import json
from datetime import date

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from apps.core import models
from . import views


class TestTodoAppAPI(TestCase):

    def setUp(self):
        self.app = models.TodoApp.objects.create(
            name='My New App',
            date=date.today(),
            description='Hey this is so cool'
        )
        self.factory = APIRequestFactory()

    def test_invalid_post(self):
        '''
        Test to verify that a post call with no date or description returns a 400 status code
        '''
        request = self.factory.post('/rest/todo-apps', {
            'name':'Hello'
        })
        view = views.ListCreateTodoApp.as_view()
        response = view(request)
        response.render()
        self.assertEqual(400, response.status_code)

    def test_create(self):
        '''
        Test to verify that a post call returns a 201 status code
        '''
        request = self.factory.post('/rest/todo-apps', {
            'name':'Hello',
            'date': date.today(),
            'description': 'So cool'
        })
        view = views.ListCreateTodoApp.as_view()
        response = view(request)
        response.render()
        self.assertEqual(201, response.status_code)

    def test_list(self):
        request = self.factory.get('/rest/todo-apps')
        view = views.ListCreateTodoApp.as_view()
        response = view(request)
        response.render()
        self.assertEqual(1, len(json.loads(response.content)))

    def test_retrieve(self):
        request = self.factory.get('/rest/todo-apps/{0}'.format(self.app.id))
        view = views.RetrieveUpdateDestroyTodoApp.as_view()
        response = view(request, pk=self.app.id)
        response.render()
        self.assertEqual(200, response.status_code)

    def test_update(self):
        # First test that the name of the app is equal to what I had set it at the beginning
        request = self.factory.get('/rest/todo-apps/{0}'.format(self.app.id))
        view = views.RetrieveUpdateDestroyTodoApp.as_view()
        response = view(request, pk=self.app.id)
        response.render()
        self.assertEqual(json.loads(response.content)['name'], self.app.name)

        # Update the model and put to the api
        new_name = 'Harold'
        self.app.name = new_name
        request = self.factory.put('/rest/todo-apps/{0}'.format(self.app.id), self.app.__dict__)
        view = views.RetrieveUpdateDestroyTodoApp.as_view()
        response = view(request, pk=self.app.id)
        response.render()
        self.assertEqual(200, response.status_code)

        # Test that the value of the model is equal to the update version
        request = self.factory.get('/rest/todo-apps/{0}'.format(self.app.id))
        view = views.RetrieveUpdateDestroyTodoApp.as_view()
        response = view(request, pk=self.app.id)
        response.render()
        self.assertEqual(json.loads(response.content)['name'], new_name)

    def test_destroy(self):
        request = self.factory.delete('/rest/todo-apps/{0}'.format(self.app.id))
        view = views.RetrieveUpdateDestroyTodoApp.as_view()
        response = view(request, pk=self.app.id)
        response.render()
        self.assertEqual(204, response.status_code)

        request = self.factory.get('/rest/todo-apps')
        view = views.ListCreateTodoApp.as_view()
        response = view(request)
        response.render()
        self.assertEqual(0, len(json.loads(response.content)))
