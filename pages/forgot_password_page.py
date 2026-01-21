from selenium.webdriver.common.by import By
from utilities.wait_utils import WaitUtils

class ForgotPasswordPage:
    EMAIL = (By.ID, "email")
    RETRIEVE_BTN = (By.ID, "form_submit")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    def enter_email(self, email):
        self.wait.wait_for_visible(self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def click_retrieve(self):
        self.wait.wait_for_clickable(self.RETRIEVE_BTN).click()

    def forgot_password(self, email):
        self.enter_email(email)
        self.click_retrieve()
