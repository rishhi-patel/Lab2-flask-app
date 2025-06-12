from app import app
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Flask!' in response.data


def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About This App' in response.data


def test_api_data(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'


def test_form_submit(client):
    response = client.post('/submit', data={'name': 'Test User'})
    assert response.status_code == 200
    assert b'Thank you, Test User!' in response.data
