import allure
import pytest
from pages.scooter_main_page import ScooterMainPage
from pages.urls import YANDEX_DZEN_URL


@allure.feature("Логотипы")
class TestLogos:

    @allure.story("Переход по логотипу Яндекса")
    @allure.title("Тест перехода на Дзен при клике на логотип Яндекса с главной страницы")
    def test_click_yandex_logo_from_main_page(self, driver):
        main_page = ScooterMainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Получить начальное количество окон"):
            initial_window_handles = main_page.get_window_handles()
            initial_window_count = len(initial_window_handles)

        with allure.step("Кликнуть по логотипу Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Дождаться открытия нового окна"):
            new_window_opened = main_page.wait_for_new_window(initial_window_handles, timeout=5)
            assert new_window_opened, "Новое окно не открылось в течение ожидаемого времени"

        with allure.step("Найти дескриптор нового окна"):
            all_window_handles = main_page.get_window_handles()
            new_window_handle = list(all_window_handles - initial_window_handles)[0]

        with allure.step("Переключиться на новое окно"):
            main_page.switch_to_window(new_window_handle)

        with allure.step(f"Дождаться, что URL нового окна - Яндекс.Дзен ({YANDEX_DZEN_URL})"):
            url_changed = main_page.wait_for_url_to_be(YANDEX_DZEN_URL, timeout=5)
            assert url_changed, f"URL не стал равным {YANDEX_DZEN_URL} в течение ожидаемого времени"
