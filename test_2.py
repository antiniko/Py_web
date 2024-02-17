import pytest
import json
import requests
from func import login, get_post

@pytest.fixture()
def new_post_token():
    response = requests.post(
        url="https://test-stand.gb.ru/api/posts",
        headers={"X-Auth-Token": login()},
        data={'title': 'Новый Заголовок', 'description': 'Новое Описание', 'content': 'Новое Содержание'}
    )
    response.raise_for_status()

    try:
        return response.json()  # Return the entire JSON response
    except ValueError:
        return response.text

def test_1():
    token = login()
    result = get_post(token)['data']
    lst = [item['id'] for item in result]
    print(lst)
    assert 98572 in lst

def test_2(new_post_token):
    print("new_post_token:", new_post_token)

    print("Raw JSON response:", new_post_token)

    post_id = new_post_token.get('id', None)
    print("Post ID:", post_id)

    assert post_id is not None, "ID поста не был найден в ответе"

    response = get_post(login())

    print("Response:", response)

    assert response.get('error') is None, f"Ошибка в ответе: {response.get('error')}"

    result = response.get('data', [])

    print("Result:", result)

    expected_description = 'Новое Описание'
    assert any(post.get('description') == expected_description for post in result), \
        f"Пост с описанием '{expected_description}' не найден на сервере"
