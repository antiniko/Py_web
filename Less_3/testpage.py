from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.common.alert import Alert

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_SUCCESS_LOGIN = (By.CSS_SELECTOR, "#app > main > nav > a > span")
    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, "#app > main > nav > ul > li:nth-child(2) > a")
    LOCATOR_CONTACT_US_MSG = (By.CSS_SELECTOR, "#app > main > div > div > h1")
    LOCATOR_CONTACT_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_CONTACT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_SEND_REPORT = (By.CSS_SELECTOR, "#contact > div.submit > button")

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click loging button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"we find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_success_text(self):
        success_text = self.find_element(TestSearchLocators.LOCATOR_SUCCESS_LOGIN, time=3)
        text = success_text.text
        logging.info(f"we find text {text} in home page {TestSearchLocators.LOCATOR_SUCCESS_LOGIN[1]}")
        return text

    def click_contact_button(self):
        logging.info("Click contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def get_contact_us_text(self):
        contact_us = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_MSG, time=3)
        text = contact_us.text
        logging.info(f"we find text {text} in contact us page {TestSearchLocators.LOCATOR_CONTACT_US_MSG[1]}")
        return text

    def enter_name_for_contact(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_CONTACT_NAME[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME)
        login_field.clear()
        login_field.send_keys(word)


    def enter_emael_for_contact(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_CONTACT_EMAIL[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content_for_contact(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_CONTENT_CONTACT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_CONTACT)
        login_field.clear()
        login_field.send_keys(word)


    def click_contact_us_button(self):
        logging.info("Click contact_us button")
        self.find_element(TestSearchLocators.LOCATOR_SEND_REPORT).click()

    def contact_us_alert(self, expected_text):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            logging.info(f"Alert text: {alert_text}")

            assert expected_text in alert_text

            # Принимаем alert (закрываем его)
            alert.accept()

            return True

        except Exception as e:
            logging.error(f"Error handling alert: {e}")
            return False
