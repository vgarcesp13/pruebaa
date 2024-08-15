import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/')
    yield driver
    driver.quit()
