import logging
import time
from testpage import OperationsHelper
from selenium.webdriver.common.alert import Alert


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("bobot2040")
    testpage.enter_pass("e37c848bc3")
    testpage.click_login_button()
    assert testpage.get_success_text() == "Home"
    testpage.click_contact_button()
    time.sleep(2) #необходимая задежрка, иначе цепляет текст с прошлой страницы
    assert testpage.get_contact_us_text() == "Contact us!"
    testpage.enter_name_for_contact("bobot")
    testpage.enter_emael_for_contact("bobot@bobot.bobot")
    testpage.enter_content_for_contact("bobot was here")
    time.sleep(1)
    testpage.click_contact_us_button()
    time.sleep(1)
    assert testpage.contact_us_alert("Form successfully submitted")

