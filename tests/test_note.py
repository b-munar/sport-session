import pytest
import json
from unittest.mock import patch
from functools import wraps

def mock_authorization(func):
    @wraps(func)
    def decorated(*args, **kwargs):
            kwargs["user"] = {"id" : "9027aff6-545e-4a1c-bbf7-9c09f6ae595c"}
            return func(*args, **kwargs)
    return decorated

patch('src.utils.authorization.authorization', mock_authorization).start()

from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_request_ping(client):
    response = client.get("/sport-session/ping")
    assert response.status_code == 200
    assert b"pong" in response.data
    
def test_request_post_register(client):
    url = "/sport-session"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "trainingDayId": "86559da0-6100-45e1-84e7-85a304a6be21",
    "FTP": 70,
    "VO": 10, 
    "RPM": 98,
    "KCAL": 300,
    "startDate": "2022-06-14T17:00:00-07:00",
    "endDate": "2022-06-14T17:30:00-07:00"
    }
    response2 = client.post(url, data=json.dumps(data), headers=headers)
    assert response2.status_code == 201
    
def test_request_get(client):
    url = "/sport-session"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "trainingDayId": "86559da0-6100-45e1-84e7-85a304a6be21",
    "FTP": 70,
    "VO": 10, 
     "RPM": 98,
    "KCAL": 300,
     "startDate": "2022-06-14T17:00:00-07:00",
    "endDate": "2022-06-14T17:30:00-07:00"
    }
    client.post(url, data=json.dumps(data), headers=headers)
    response = client.get("/sport-session")
    assert response.status_code == 200
    assert b"sessions" in response.data
    
def test_request_get_avg(client):
    url = "/sport-session/avg"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "trainingDayId": "86559da0-6100-45e1-84e7-85a304a6be21",
    "FTP": 70,
    "VO": 10, 
     "RPM": 98,
    "KCAL": 300,
     "startDate": "2022-06-14T17:00:00-07:00",
    "endDate": "2022-06-14T17:30:00-07:00"
    }
    client.post(url, data=json.dumps(data), headers=headers)
    response = client.get("/sport-session/avg")
    assert response.status_code == 200
    assert b"average_results" in response.data

