from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
from locators import *

class OrderPage(BasePage):

    def set_first_name(self, name):
        self.driver.find_element(*FIRST_NAME_FIELD).send_keys(name)

    def set_last_name(self, surname):
        self.driver.find_element(*LAST_NAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*ADDRESS_FIELD).send_keys(address)

    def set_metro_station(self, station):
        station_input = self.find_element(METRO_STATION_FIELD)
        station_input.click()
        station_input.clear()
        station_input.send_keys(station)   
        option_locator = (METRO_STATION_OPTION_TEMPLATE) 
        option_element = self.wait.until(EC.element_to_be_clickable(option_locator))
        option_element.click()

    def set_phone_number(self, phone):
        self.driver.find_element(*PHONE_NUMBER_FIELD).send_keys(phone)

    def click_next_button(self):
        next_button = self.wait.until(EC.element_to_be_clickable(NEXT_BUTTON))
        next_button.click()

    def set_delivery_date(self, delivery_date):
        delivery_date_field = self.wait.until(EC.element_to_be_clickable(WHEN_TO_DELIVER_FIELD))
        delivery_date_field.click()
        option_locator = (WHEN_TO_DELIVER_OPTION)
        option_element = self.wait.until(EC.element_to_be_clickable(option_locator))
        option_element.click()
       
    def set_rental_period(self, rental_period):
        rental_period_dropdown = self.wait.until(EC.element_to_be_clickable(RENTAL_PERIOD_DROPDOWN))
        rental_period_dropdown.click()
        option_locator = (RENTAL_PERIOD_OPTION_TEMPLATE) 
        option_element = self.wait.until(EC.element_to_be_clickable(option_locator))
        option_element.click()

    def select_color_black(self):
        self.driver.find_element(*COLOR_CHECKBOX_BLACK).click()

    def select_color_grey(self):
        self.driver.find_element(*COLOR_CHECKBOX_GREY).click()

    def set_comment(self, comment):
        self.driver.find_element(*COMMENT_FIELD).send_keys(comment)

    def click_final_order_button(self):
        order_button = self.wait.until(EC.element_to_be_clickable(ORDER_BUTTON_FINAL))
        order_button.click()

    def click_confirm_order(self):
        confirm_button = self.wait.until(EC.element_to_be_clickable(CONFIRM_ORDER_BUTTON))
        confirm_button.click()

    def click_order_status_button(self):
        order_status_button = self.wait.until(EC.element_to_be_clickable(ORDER_STATUS_BUTTON))
        order_status_button.click()

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