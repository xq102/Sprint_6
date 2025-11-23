from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from locators import COOKIE_ACCEPT_BUTTON

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"
        self.wait = WebDriverWait(driver, 15)

    def open(self, url: str = ""):
        self.driver.get(self.base_url + url)
        self.accept_cookies()

    def find_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return elements

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def accept_cookies(self):
        try:
            short_wait = WebDriverWait(self.driver, 3)
            cookie_button = short_wait.until(EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON))
            cookie_button.click()
        except TimeoutException:
            pass
