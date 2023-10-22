from src.pages.create_account_page import *
from src.utilities import *
import pytest

logfile = f"{ROOT_DIR}/logs/{get_str_day()}_student_registration.log"
log = create_logger(logfile)


@pytest.mark.regression
def test_register_page(driver):
    # test data:
    host = "https://demoqa.com/register"
    first_name = "Polat"
    last_name = "Cucurela"
    username = "user4545"
    password = "Password321!"

    register_page = AccountCreation(driver)

    log.info("#1 Opening the registering page...")
    driver.get(host)
    disable_google_ads(driver)

    register_page.enter_first_name(first_name)
    register_page.enter_last_name(last_name)
    register_page.enter_username(username)
    register_page.enter_password(password)
    register_page.check_recaptcha()
    register_page.register_button()
    # register_page.alert()



