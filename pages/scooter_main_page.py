from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators import *
import allure


class ScooterMainPage(BasePage):

    @allure.step("Клик по верхней кнопке заказа")
    def click_order_button_top(self):
        self.click_element(ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке заказа")
    def click_order_button_bottom(self):
        self.click_element(ORDER_BUTTON_BOTTOM)

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_element(SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(YANDEX_LOGO)

    @allure.step("Получение текста заголовков FAQ")
    def get_faq_headers(self):
        headers = self.find_elements(FAQ_QUESTION_HEADERS)
        return [header.text for header in headers]

    @allure.step("Получение текста ответа FAQ под индексом {index}")
    def get_faq_body_text(self, index):
        headers = self.find_elements(FAQ_QUESTION_HEADERS)
        if not (0 <= index < len(headers)):
            return ""

        target_header = headers[index]
        target_panel_id = self.get_attribute(target_header, "aria-controls")
        self.click_on_element(target_header)
        target_panel_locator = (By.ID, target_panel_id)
        self.wait_for_locator_to_be_visible(target_panel_locator)
        target_panel = self.find_element(target_panel_locator)

        try:
            text_paragraph = self.find_element_within(target_panel, (By.TAG_NAME, "p"))
            return text_paragraph.text
        except:
            return ""

    @allure.step("Клик по заголовку FAQ под индексом {index}")
    def click_faq_header(self, index):
        headers = self.find_elements(FAQ_QUESTION_HEADERS)
        if 0 <= index < len(headers):
            header_to_click = headers[index]
            self.click_on_element(header_to_click)

    @allure.step("Ожидание появления раздела FAQ и прокрутка до него")
    def wait_for_faq(self):
        faq_element = self.find_element(FAQ_SECTION)
        self.scroll_into_view(faq_element)
        self.wait_for_locator_to_be_visible(FAQ_SECTION)
