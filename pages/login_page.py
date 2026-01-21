from selenium.webdriver.common.by import By
from utilities.wait_utils import WaitUtils

class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MSG = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    def enter_username(self, username):
        self.wait.wait_for_visible(self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait.wait_for_visible(self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.wait.wait_for_clickable(self.LOGIN_BTN).click()

    def get_error_message(self):
        return self.wait.wait_for_visible(self.ERROR_MSG).text

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
