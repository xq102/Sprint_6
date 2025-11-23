from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators import *

class ScooterMainPage(BasePage):

    def click_order_button_top(self):
        self.click_element(ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click_element(ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click_element(SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(YANDEX_LOGO)

    def get_faq_headers(self):
        headers = self.driver.find_elements(*FAQ_QUESTION_HEADERS)
        return [header.text for header in headers]

    def get_faq_body_text(self, index):
        headers = self.driver.find_elements(*FAQ_QUESTION_HEADERS)
        if not (0 <= index < len(headers)):
            return ""

        target_header = headers[index]
        target_panel_id = target_header.get_attribute("aria-controls")

        target_header.click()

        target_panel_locator = (By.ID, target_panel_id)
        self.wait.until(EC.visibility_of_element_located(target_panel_locator))

        target_panel = self.driver.find_element(*target_panel_locator)

        try:
            text_paragraph = target_panel.find_element(By.TAG_NAME, "p")
            return text_paragraph.text
        except:
            return ""

    def click_faq_header(self, index):
        headers = self.driver.find_elements(*FAQ_QUESTION_HEADERS)
        if 0 <= index < len(headers):
            header_to_click = headers[index]
            self.wait.until(EC.element_to_be_clickable(header_to_click))
            header_to_click.click()

    def wait_for_faq(self):
        faq_element = self.find_element(FAQ_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", faq_element)
        self.wait.until(EC.visibility_of_element_located(FAQ_SECTION))
