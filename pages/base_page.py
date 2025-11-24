from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from locators import COOKIE_ACCEPT_BUTTON
import allure
from .urls import BASE_URL


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = BASE_URL
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открытие страницы {url}")
    def open(self, url: str = ""):
        self.driver.get(self.base_url + url)
        self.accept_cookies()

    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    @allure.step("Поиск нескольких элементов по локатору")
    def find_elements(self, locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return elements

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step("Ввод текста '{text}' в поле {locator}")
    def send_keys_to_element(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Принятие файлов cookie")
    def accept_cookies(self):
        try:
            short_wait = WebDriverWait(self.driver, 3)
            cookie_button = short_wait.until(EC.element_to_be_clickable(COOKIE_ACCEPT_BUTTON))
            cookie_button.click()
        except TimeoutException:
            pass

    @allure.step("Получение дескрипторов всех окон")
    def get_window_handles(self):
        return set(self.driver.window_handles)

    @allure.step("Ожидание открытия нового окна (ожидание {timeout} сек)")
    def wait_for_new_window(self, initial_handles_set, timeout=5):
        try:
            self.wait.until(
                lambda d: len(d.window_handles) > len(initial_handles_set)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Переключение на окно с дескриптором {window_handle}")
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    @allure.step("Ожидание изменения URL в текущем окне на {expected_url}")
    def wait_for_url_to_be(self, expected_url, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.url_to_be(expected_url))
            return True
        except TimeoutException:
            return False
