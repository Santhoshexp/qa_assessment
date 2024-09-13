"""Module to test the frontend service"""

import requests

def test_response():
    """Method to validate the response code"""
    url = "http://127.0.0.1:56563"
    response = requests.get(url,timeout=60)
    assert response.status_code == 200
    assert "<h1>Hello from the Backend!</h1>" in response.text

def test_content():
    """Method to validate the response content"""
    url = "http://127.0.0.1:56563"
    response = requests.get(url,timeout=60)
    assert "<h1>Hello from the Backend!</h1>" == response.text
