import logging
import time
from testpage import OperationsHelper
from send_log import send_email_report

def test_step0(browser):
    logging.info("Test0 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert  testpage.get_error_text() == "401"

def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("bobot2040")
    testpage.enter_pass("e37c848bc3")
    testpage.click_login_button()
    assert testpage.get_success_text() == "Blog"
    testpage.click_contact_button()
    time.sleep(1) #необходимая задежрка, иначе цепляет текст с прошлой страницы
    assert testpage.get_contact_us_text() == "Contact us!"
    testpage.enter_name_for_contact("bobot")
    testpage.enter_emael_for_contact("bobot@bobot.bobot")
    testpage.enter_content_for_contact("bobot was here")
    testpage.click_contact_us_button()
    time.sleep(1)
    assert testpage.contact_us_alert("Form successfully submitted")

def teardown():
    send_email_report()
