# locators.py
from selenium.webdriver.common.by import By

# --- Главная страница "Яндекс.Самокат" ---
# Кнопка "Заказать" вверху страницы
ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
# Кнопка "Заказать" внизу страницы 
ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
# Логотип "Самокат" в шапке
SCOOTER_LOGO = (By.XPATH, "//img[@src='/assets/scooter.svg']")
# Логотип "Яндекс" в шапке
YANDEX_LOGO = (By.XPATH, "//img[@src='/assets/ya.svg']")
# Кнопка принятия куки
COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
# Контейнер с вопросами FAQ
FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
# Заголовки вопросов в FAQ
FAQ_QUESTION_HEADERS = (By.CLASS_NAME, "accordion__button")
# Тела вопросов в FAQ (ответы)
FAQ_QUESTION_BODIES = (By.CLASS_NAME, "accordion__panel")

# --- Форма заказа  ---
# Поле ввода "Имя"
FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
# Поле ввода "Фамилия"
LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
# Поле ввода "Адрес"
ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
# Поле ввода "Станция метро"
METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
# Шаблон XPATH для элемента списка станций метро 
METRO_STATION_OPTION_TEMPLATE = (By.XPATH, "//div[text()='Черкизовская']/parent::button")
# Поле ввода "Телефон"
PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
# Кнопка "Далее" на первой части формы
NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")
# Поле ввода "Когда привезти самокат" (дата)
WHEN_TO_DELIVER_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
# Выпадающий календарь "Когда привезти самокат" (дата)
WHEN_TO_DELIVER_OPTION = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--001') and contains(@aria-label, '1-е')]")
# Выпадающий список "Срок аренды"
RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-placeholder']")
# Шаблон XPATH для опции срока аренды (ИСПРАВЛЕНО: строка)
RENTAL_PERIOD_OPTION_TEMPLATE = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
# Чекбокс выбора цвета "Чёрный жемчуг"
COLOR_CHECKBOX_BLACK = (By.ID, "black")
# Чекбокс выбора цвета "Серая безысходность"
COLOR_CHECKBOX_GREY = (By.ID, "grey")
# Поле ввода "Комментарий для курьера"
COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
# Кнопка "Заказать" на второй части формы
ORDER_BUTTON_FINAL = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
# Кнопка "Да" в окне подтверждения заказа
CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
# Кнопка "Посмотреть статус"
ORDER_STATUS_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")
# Кнопка "Посмотреть"
STATUS_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть']")
# Кнопка "Отменить"
ORDER_CANCEL_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Отменить']")


# Окно с подтверждением заказа
SUCCESS_ORDER = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']")
# Заголовок в окне подтверждения заказа
SUCCESS_MESSAGE = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
SUCCESS_ORDER_MODAL = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']")
# Заголовок в окне подтверждения заказа
SUCCESS_MESSAGE_HEADER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
# Кнопка "Заказ оформлен" 
SUCCESS_ORDER_CONFIRMATION_TEXT = (By.XPATH, "//div[@class='Order_Text__2broe']")
# Кнопка "ОК" в модальном окне 
SUCCESS_MODAL_OK_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")