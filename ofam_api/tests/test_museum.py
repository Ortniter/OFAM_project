import pytest

from django.urls import reverse


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.dajngo_db
def test_unauthorized_request(api_client):
    url = reverse('need-token-url')
    response = api_client(url)
    assert response.status_code == 401
