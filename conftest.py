import pytest
import requests
import yaml

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    response = requests.post(url="https://test-stand.gb.ru/gateway/login",
                             data={'username': data['login'], 'password': data['password']})
    return response.json()['token']