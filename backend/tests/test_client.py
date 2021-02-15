import requests
from app import client

def test_response_code():
    obj = client.Client()
    response = requests.get(obj.URL)
    data = response.json()
    assert data['cod'] == '200'

def test_request_weather():
    obj = client.Client()
    response = obj.request_weather()
    assert len(response[0].keys()) == 9