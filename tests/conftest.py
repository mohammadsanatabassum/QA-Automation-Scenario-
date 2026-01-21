import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.logger import get_logger

logger = get_logger()

@pytest.fixture
def driver():
    """
    Works both in:
    ✅ Local Machine (opens normal chrome)
    ✅ GitHub Actions CI (headless chrome)
    """

    logger.info("Launching browser")

    options = Options()

    # Detect CI environment (GitHub Actions sets CI=true)
    is_ci = os.environ.get("CI") == "true"

    if is_ci:
        # ✅ Headless Chrome settings for CI
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        logger.info("Running in CI mode (headless)")
    else:
        # ✅ Normal browser settings for local run
        options.add_argument("--start-maximized")
        logger.info("Running in local mode (headed)")

    driver = webdriver.Chrome(options=options)

    yield driver

    logger.info("Closing browser")
    driver.quit()
