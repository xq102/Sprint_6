import allure
import pytest
from pages.scooter_main_page import ScooterMainPage

@allure.feature("FAQ")
class TestFAQ:

    @allure.story("Проверка раскрытия вопросов")
    @pytest.mark.parametrize("question_index, expected_answer", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_expand_faq_question(self, driver, question_index, expected_answer):
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
