import allure
import pytest
from pages.scooter_main_page import ScooterMainPage
from pages.order_page import OrderPage


@allure.epic("Web UI Tests")
@allure.feature("Заказ самоката")
class TestOrderFlow:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_page = ScooterMainPage(driver)
        self.order_page = OrderPage(driver)
        self.driver = driver

    def fill_and_submit_order_form(self, first_name, last_name, address, metro, phone, delivery_date, rental_period, color, comment):
        self.order_page.set_first_name(first_name)
        self.order_page.set_last_name(last_name)
        self.order_page.set_address(address)
        self.order_page.set_metro_station(metro)
        self.order_page.set_phone_number(phone)
        self.order_page.click_next_button()

        self.order_page.set_delivery_date(delivery_date)
        self.order_page.set_rental_period(rental_period)
        if color == "black":
            self.order_page.select_color_black()
        elif color == "grey":
            self.order_page.select_color_grey()
        self.order_page.set_comment(comment)
        self.order_page.click_final_order_button()

    @allure.story("Позитивный сценарий заказа через нижнюю кнопку")
    @allure.title("Тест заказа самоката через нижнюю кнопку с данными {first_name} {last_name}")
    @pytest.mark.parametrize("first_name, last_name, address, metro, phone, delivery_date, rental_period, color, comment", [
        ("Анна", "Петрова", "пр-т Мира, д. 100", "Черкизовская", "+79876543210", "05.11.2025", "сутки", "grey", "Позвонить за 10 минут"),
    ])
    def test_order_flow_from_bottom_button(self, first_name, last_name, address, metro, phone, delivery_date, rental_period, color, comment):
        with allure.step("Открыть главную страницу"):
            self.main_page.open()

        with allure.step("Прокрутить до нижней кнопки заказа"):
            self.main_page.wait_for_faq()

        with allure.step("Кликнуть нижнюю кнопку заказа"):
            self.main_page.click_order_button_bottom()

        with allure.step("Заполнить и отправить форму заказа"):
            self.fill_and_submit_order_form(first_name, last_name, address, metro, phone, delivery_date, rental_period, color, comment)

        with allure.step("Подтвердить заказ"):
            self.order_page.click_confirm_order()

        with allure.step("Проверить, что модальное окно с подтверждением отображается"):
            assert self.order_page.is_success_modal_displayed(), f"Модальное окно с подтверждением заказа не отображается после заказа {first_name} {last_name}."
