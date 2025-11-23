import allure
import pytest
from pages.scooter_main_page import ScooterMainPage
from pages.order_page import OrderPage

@allure.feature("Логотипы")
class TestScooterLogo:

    @allure.story("Переход на главную по логотипу Самокат")
    @allure.title("Тест перехода на главную страницу при клике на логотип Самокат после перехода на страницу заказа")
    def test_click_scooter_logo_after_going_to_order_page(self, driver):
        main_page = ScooterMainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Перейти на страницу заказа, кликнув верхнюю кнопку 'Заказать'"):
            main_page.click_order_button_top()

        with allure.step("Кликнуть по логотипу Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверить, что вернулись на главную страницу"):
            current_url = driver.current_url.rstrip('/')
            expected_url = main_page.base_url.rstrip('/')

            assert current_url == expected_url, \
                f"После нажатия на логотип Самоката с другой страницы ожидаемый URL: {expected_url}, но был: {current_url}"
