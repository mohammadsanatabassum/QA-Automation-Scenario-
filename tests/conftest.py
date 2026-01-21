import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.logger import get_logger

logger = get_logger()

@pytest.fixture
def driver():
    logger.info("Launching browser")

    options = Options()
    options.add_argument("--start-maximized")

    # ✅ Selenium Manager will automatically download and use correct ChromeDriver
    driver = webdriver.Chrome(options=options)

    yield driver

    logger.info("Closing browser")
    driver.quit()
