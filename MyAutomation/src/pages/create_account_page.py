from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from conftest import driver
from src.pages.base_page import BasePage
from src.utilities import *

logfile = f"{ROOT_DIR}/logs/{get_str_day()}.log"
log = create_logger(logfile)


class AccountCreation(BasePage):
    """ Page Object Model of forms page, defines all attributes and methods of the page(Building blocks).
    """

    # LOCATORS(Attributes)
    recaptcha_xpath = "//div[@class ='recaptcha-checkbox-checkmark']"
    host = "https://demoqa.com/register"
    register_xpath = "//button[@id='register']"


    def enter_first_name(self, first_name):
        log.info("#2 Entering first name...")
        self.enter_text_by_id('firstname', first_name)

    def enter_last_name(self, last_name):
        log.info("#3 Entering last name...")
        self.enter_text_by_id('firstname', last_name)

    def enter_username(self, user_name):
        log.info("#4 Entering username...")
        self.enter_text_by_id('userName', user_name)

    def enter_password(self, password):
        log.info("Entering password...")
        self.enter_text_by_id('password', password)

    def check_recaptcha(self):
        log.info("Clicking recaptcha...")
        self.click_element_by_xpath(self.recaptcha_xpath)


    def register_button(self):
        # log.info("Clicking register button...")
        # self.click_element_by_xpath(self.register_xpath)
        log.info('Clicking the element by XPATH..')
        element = self.wdwait.until(EC.element_to_be_clickable((By.XPATH, self.register_xpath)))
        element.click()

    def alert(self):
        log.info('Handling an alert ....')
        ok_alert = self.driver.switch_to.alert
        ok_alert.accept()












