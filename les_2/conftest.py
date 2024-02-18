import pytest
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from module import Site


@pytest.fixture
def element_locators():
    locators = {
        "login": "//*[@id='login']/div[1]/label/input",
        "password": "//*[@id='login']/div[2]/label/input",
        "button": "button",
        "error_message": "//*[@id='app']/main/div/div/div[2]/h2",
        "success_message": "//*[@id='app']/main/div/div[1]/h1",
        "create_post_button": "#create-btn",
        "post_title_input": "//*[@id='create-item']/div/div/div[1]/div/label/input",
        "post_description_input": "//*[@id='create-item']/div/div/div[2]/div/label/span/textarea",
        "post_content_input": "//*[@id='create-item']/div/div/div[3]/div/label/span/textarea",
        "post_save_button": "#create-item > div > div > div:nth-child(7) > div > button",
        "check_new_post_title": "//*[@id='app']/main/div/div[3]/div[1]/a[1]/h2",

    }
    return locators


@pytest.fixture
def expected_result():
    return {"expected_text": "401"}

@pytest.fixture
def expected_success():
    return {"expected_success": "Blog"}

@pytest.fixture
def new_blog():
    return {"new_blog": "Заголовок поста"}

@pytest.fixture
def test_data():
    with open("testdata.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture
def site(request, test_data):
    site_instance = Site(test_data["address"])

    def fin():
        site_instance.close()

    request.addfinalizer(fin)

    return site_instance
