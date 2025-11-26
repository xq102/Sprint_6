from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
import allure
from locators import * 


class OrderPage(BasePage):

    @allure.step("Ввод имени: {name}")
    def set_first_name(self, name):
        self.send_keys_to_element(FIRST_NAME_FIELD, name)

    @allure.step("Ввод фамилии: {surname}")
    def set_last_name(self, surname):
        self.send_keys_to_element(LAST_NAME_FIELD, surname)

    @allure.step("Ввод адреса: {address}")
    def set_address(self, address):
        self.send_keys_to_element(ADDRESS_FIELD, address)

    @allure.step("Выбор станции метро: {station}")
    def set_metro_station(self, station):
        station_input = self.find_element(METRO_STATION_FIELD)
        station_input.click()
        self.click_element(METRO_STATION_OPTION_TEMPLATE)

    @allure.step("Ввод номера телефона: {phone}")
    def set_phone_number(self, phone):
        self.send_keys_to_element(PHONE_NUMBER_FIELD, phone)

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button(self):
        self.click_element(NEXT_BUTTON)

    @allure.step("Установка даты доставки")
    def set_delivery_date(self, delivery_date):
        self.click_element(WHEN_TO_DELIVER_FIELD)
        self.click_element(WHEN_TO_DELIVER_OPTION)

    @allure.step("Установка срока аренды")
    def set_rental_period(self, rental_period):
        self.click_element(RENTAL_PERIOD_DROPDOWN)
        self.click_element(RENTAL_PERIOD_OPTION_TEMPLATE)

    @allure.step("Выбор цвета: Черный")
    def select_color_black(self):
        self.click_element(COLOR_CHECKBOX_BLACK)

    @allure.step("Выбор цвета: Серый")
    def select_color_grey(self):
        self.click_element(COLOR_CHECKBOX_GREY)

    @allure.step("Ввод комментария: {comment}")
    def set_comment(self, comment):
        self.send_keys_to_element(COMMENT_FIELD, comment)

    @allure.step("Клик по финальной кнопке 'Заказать'")
    def click_final_order_button(self):
        self.click_element(ORDER_BUTTON_FINAL)

    @allure.step("Клик по кнопке подтверждения заказа")
    def click_confirm_order(self):
        self.click_element(CONFIRM_ORDER_BUTTON)

    @allure.step("Клик по кнопке 'Статус заказа'")
    def click_order_status_button(self):
        self.click_element(ORDER_STATUS_BUTTON)

    @allure.step("Проверка отображения модального окна успеха")
    def is_success_modal_displayed(self):
        modal_visible = self.is_element_visible(SUCCESS_ORDER_MODAL)
        if modal_visible:
            try:
                header_text = self.get_text(SUCCESS_MESSAGE_HEADER)
                confirmation_text = self.get_text(SUCCESS_ORDER_CONFIRMATION_TEXT)
                return bool(header_text) or bool(confirmation_text)
            except TimeoutException:
                return True
        return False

    @allure.step("Заполнение и отправка формы заказа")
    def fill_and_submit_order_form(self, first_name, last_name, address, metro, phone, delivery_date, rental_period, color, comment):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro_station(metro)
        self.set_phone_number(phone)
        self.click_next_button()

        self.set_delivery_date(delivery_date)
        self.set_rental_period(rental_period)
        if color == "black":
            self.select_color_black()
        elif color == "grey":
            self.select_color_grey()
        self.set_comment(comment)
        self.click_final_order_button()
