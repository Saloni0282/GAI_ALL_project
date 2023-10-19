import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert b"Welcome to the Todo API!" in response.data

def test_get_todos_empty(client):
    response = client.get('/todos')
    assert b"[]" in response.data
