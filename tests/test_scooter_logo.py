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
            current_url = main_page.get_current_url()
            expected_url = main_page.base_url 
    
            normalized_current = current_url.rstrip('/')
            normalized_expected = expected_url.rstrip('/')

            assert normalized_current == normalized_expected, \
                f"После нажатия на логотип Самоката с другой страницы ожидаемый URL: {normalized_expected}, но был: {normalized_current}"
