import allure
import pytest
from pages.scooter_main_page import ScooterMainPage
from pages.order_page import OrderPage


@allure.epic("Web UI Tests")
@allure.feature("Заказ самоката")
class TestOrderFlow:

    @allure.story("Позитивный сценарий заказа через верхнюю кнопку")
    @allure.title("Тест заказа самоката через верхнюю кнопку с данными {first_name} {last_name}")
    @pytest.mark.parametrize("first_name, last_name, address, metro, phone, delivery_date, rental_period, color, comment", [
        ("Иван", "Иванов", "ул. Тестовая, д. 1", "Черкизовская", "+79991234567", "01.10.2025", "двое суток", "black", "Оставьте у двери"),
    ])
    def test_order_flow_from_top_button(self, driver, first_name, last_name, address, metro, phone, delivery_date, rental_period, color, comment):
        main_page = ScooterMainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Кликнуть верхнюю кнопку заказа"):
            main_page.click_order_button_top()

        with allure.step("Заполнить и отправить форму заказа"):
            order_page.fill_and_submit_order_form(first_name, last_name, address, metro, phone, delivery_date, rental_period, color, comment)

        with allure.step("Подтвердить заказ"):
            order_page.click_confirm_order()

        with allure.step("Проверить, что модальное окно с подтверждением отображается"):
            assert order_page.is_success_modal_displayed(), f"Модальное окно с подтверждением заказа не отображается после заказа {first_name} {last_name}."
