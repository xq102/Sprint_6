import allure
import pytest
from pages.scooter_main_page import ScooterMainPage
from data import FAQ_DATA


@allure.feature("FAQ")
class TestFAQ:

    @allure.story("Проверка раскрытия вопросов")
    @pytest.mark.parametrize("faq_item", FAQ_DATA)
    def test_expand_faq_question(self, driver, faq_item):
        question_index = faq_item["question_index"]
        expected_answer = faq_item["expected_answer"]

        main_page = ScooterMainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Прокрутить до раздела FAQ"):
            main_page.wait_for_faq()

        with allure.step(f"Кликнуть на вопрос под индексом {question_index}"):
            main_page.click_faq_header(question_index)

        with allure.step(f"Получить текст ответа на вопрос под индексом {question_index}"):
            actual_answer = main_page.get_faq_body_text(question_index)

        with allure.step(f"Проверить, что текст ответа соответствует ожидаемому"):
            assert actual_answer == expected_answer, \
                f"Для вопроса под индексом {question_index} ожидаемый ответ: '{expected_answer}', но получен: '{actual_answer}'"
