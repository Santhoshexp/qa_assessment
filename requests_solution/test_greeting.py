"""Module to test the frontend service"""

import requests

URL = "http://127.0.0.1:61673"

def test_response():
    """Method to validate the response code"""
    response = requests.get(URL,timeout=60)
    assert response.status_code == 200

def test_content():
    """Method to validate the response content"""
    response = requests.get(URL,timeout=60)
    assert "<h1>Hello from the Backend!</h1>" == response.text
