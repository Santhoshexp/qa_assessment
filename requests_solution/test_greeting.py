"""Module"""

import requests

def test_response():
    """Method"""
    url = "http://127.0.0.1:56563"
    response = requests.get(url,timeout=60)
    assert response.status_code == 200
    assert "<h1>Hello from the Backend!</h1>" in response.text

def test_content():
    """Method"""
    url = "http://127.0.0.1:56563"
    response = requests.get(url,timeout=60)
    assert "<h1>Hello from the Backend!</h1>" == response.text
