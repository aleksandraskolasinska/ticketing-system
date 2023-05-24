import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from tickets.models import Ticket
from django.middleware.csrf import get_token
import requests


@pytest.fixture
def create_user():
    user = User.objects.create_user(
        username='exampleuser',
        password='somepasswordo',
    )
    return user

@pytest.fixture
def authenticated_client(client, create_user):
    client.login(username='exampleuser', password='somepasswordo')
    return client


@pytest.mark.django_db
def test_ticket_creation_performance_redirect(benchmark, client, settings):
    response = client.post('/login/', {'username': 'exampleuser', 'password': 'somepasswordo'})
    csrf_token = response.cookies['csrftoken']

    url = '/tickets/create/'
    data = {'title': 'Test title', 'ticket_content': 'test description'}

    headers = {'HTTP_X_CSRFTOKEN': csrf_token}

    result = benchmark(client.post, url, data=data, **headers)
    print(result)

    assert result.status_code == 302  
