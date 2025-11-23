import allure
import pytest
from pages.scooter_main_page import ScooterMainPage

@allure.feature("Логотипы")
class TestLogos:

    @allure.story("Переход по логотипу Яндекса")
    @allure.title("Тест перехода на Дзен при клике на логотип Яндекса с главной страницы")
    def test_click_yandex_logo_from_main_page(self, driver):
        main_page = ScooterMainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Получить начальное количество окон"):
            initial_window_handles = set(driver.window_handles)
            initial_window_count = len(initial_window_handles)

        with allure.step("Кликнуть по логотипу Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Дождаться открытия нового окна"):
            from selenium.webdriver.support.ui import WebDriverWait
            wait = WebDriverWait(driver, 5)
            wait.until(lambda d: len(d.window_handles) > initial_window_count)

        with allure.step("Найти дескриптор нового окна"):
            all_window_handles = set(driver.window_handles)
            new_window_handle = list(all_window_handles - initial_window_handles)[0]

        with allure.step("Переключиться на новое окно"):
            driver.switch_to.window(new_window_handle)

        with allure.step("Дождаться, что URL нового окна - Яндекс.Дзен"):
            from selenium.webdriver.support import expected_conditions as EC
            wait = WebDriverWait(driver, 5)
            wait.until(EC.url_to_be("https://dzen.ru/?yredirect=true"))
