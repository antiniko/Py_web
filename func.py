import requests
import yaml

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)

def login():
    response = requests.post(url="https://test-stand.gb.ru/gateway/login",
                             data={'username': data['login'], 'password': data['password']})
    return response.json()['token']

def get_post(token):
    resource = requests.get(
        "https://test-stand.gb.ru/api/posts",
        headers={"X-Auth-Token": token}
    )
    print("Raw Response:", resource.text)  # Add this line for debugging
    return resource.json()


print(get_post(login()))
