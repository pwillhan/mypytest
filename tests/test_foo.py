import os

import requests


def test_foo():
    assert 4 / 2 == 2


def test_get_request():
    url = "https://httpbin.org/get"

    payload = {}
    headers = {
        'accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200


def test_env_var_secrets():
    password = os.environ["PASSWORD"]
    assert password == 'abc123'
