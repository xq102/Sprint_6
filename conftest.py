import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="function")
def driver():
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")
    service = FirefoxService(GeckoDriverManager().install())
    driver_instance = webdriver.Firefox(service=service, options=firefox_options)
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()
    