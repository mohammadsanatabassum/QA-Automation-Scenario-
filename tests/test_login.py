import json
import pytest

from pages.login_page import LoginPage
from config.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD
from utilities.logger import get_logger

logger = get_logger()

def load_login_data():
    with open("data/login_data.json", "r") as f:
        return json.load(f)

@pytest.mark.smoke
def test_login_valid_credentials(driver):
    logger.info("Valid login test started")

    driver.get(BASE_URL)
    login_page = LoginPage(driver)

    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    # Assertion: successful login page contains Secure Area
    assert "Secure Area" in driver.page_source
    logger.info("Valid login test passed")


@pytest.mark.regression
@pytest.mark.parametrize("data", load_login_data())
def test_login_invalid_credentials(driver, data):
    logger.info(f"Invalid login test started: {data}")

    driver.get(BASE_URL)
    login_page = LoginPage(driver)

    login_page.login(data["username"], data["password"])
    error_msg = login_page.get_error_message()

    assert data["expected_error"] in error_msg
    logger.info("Invalid login test passed")
