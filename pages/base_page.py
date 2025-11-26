from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
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

    @allure.step("Прокрутка к элементу {element}")
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Получение атрибута '{attribute_name}' у элемента")
    def get_attribute(self, element, attribute_name):
        return element.get_attribute(attribute_name)

    @allure.step("Поиск элемента {locator} внутри родительского элемента {parent_element}")
    def find_element_within(self, parent_element, locator):
        return parent_element.find_element(*locator)

    @allure.step("Поиск нескольких элементов {locator} внутри родительского элемента {parent_element}")
    def find_elements_within(self, parent_element, locator):
        return parent_element.find_elements(*locator)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Клик по элементу {element}")
    def click_on_element(self, element):
        element.click()

    @allure.step("Ожидание, что элемент {element} кликабелен")
    def wait_for_element_to_be_clickable(self, element, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.element_to_be_clickable(element))
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="WaitForElementToBeClickableTimeout", attachment_type=allure.attachment_type.PNG)
            raise

    @allure.step("Ожидание, что элемент {element} видим")
    def wait_for_element_to_be_visible(self, element, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of(element))
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="WaitForElementToBeVisibleTimeout", attachment_type=allure.attachment_type.PNG)
            raise

    @allure.step("Ожидание видимости элемента по локатору {locator}")
    def wait_for_locator_to_be_visible(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="WaitForLocatorVisibleTimeout", attachment_type=allure.attachment_type.PNG)
            raise

    @allure.step("Ожидание присутствия элемента в DOM по локатору {locator}")
    def wait_for_locator_to_be_present(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="WaitForLocatorPresentTimeout", attachment_type=allure.attachment_type.PNG)
            raise
