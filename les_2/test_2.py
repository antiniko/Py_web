import pytest
from module import Site
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("element_locators", "expected_result", "test_data")
# def test_step1(element_locators, expected_result, test_data, site):
#     # логин
#     login_input = site.find_element("xpath", element_locators["login"])
#     login_input.send_keys("test")
#     # пароль
#     password_input = site.find_element("xpath", element_locators["password"])
#     password_input.send_keys("test")
#     # кнопка логина
#     button = site.find_element("css", element_locators["button"])
#     button.click()
#     # ошибка логина
#     error_label = site.find_element("xpath", element_locators["error_message"])
#     assert error_label.text == expected_result["expected_text"]
#
# def test_step2(element_locators, expected_result, test_data, site, expected_success):
#     # Вводим новые данные из конфигурационного файла
#     login_input = site.find_element("xpath", element_locators["login"])
#     login_input.send_keys(test_data["login"])
#
#     password_input = site.find_element("xpath", element_locators["password"])
#     password_input.send_keys(test_data["password"])
#
#     button = site.find_element("css", element_locators["button"])
#     button.click()
#
#     success_message = site.find_element("xpath", element_locators["success_message"])
#     assert success_message.text == expected_success["expected_success"]
#
    # создание поста
def test_step3(element_locators, expected_result, test_data, site, expected_success, new_blog):
    login_input = site.find_element("xpath", element_locators["login"])
    login_input.send_keys(test_data["login"])

    password_input = site.find_element("xpath", element_locators["password"])
    password_input.send_keys(test_data["password"])

    button = site.find_element("css", element_locators["button"])
    button.click()

    success_message = site.find_element("xpath", element_locators["success_message"])
    assert success_message.text == expected_success["expected_success"]
    # задержка перед созданием поста

    site.wait(10)
    create_post_button = site.find_element("css", element_locators["create_post_button"])
    create_post_button.click()

    site.wait(5)
    post_title_input = site.find_element("xpath", element_locators["post_title_input"])
    post_title_input.send_keys("Заголовок поста")
    site.wait(5)

    post_description_input = site.find_element("xpath", element_locators["post_description_input"])
    post_description_input.send_keys("Описание поста")
    site.wait(5)

    post_content_input = site.find_element("xpath", element_locators["post_content_input"])
    post_content_input.send_keys("Текст поста")
    site.wait(5)
    #
    post_save_button = site.find_element("css", element_locators["post_save_button"])
    post_save_button.click()
    site.wait(5)

    new_blog_text = site.find_element("xpath", element_locators["check_new_post_title"]).text
    expected_new_blog_text = new_blog["new_blog"]
    assert new_blog_text == expected_new_blog_text

