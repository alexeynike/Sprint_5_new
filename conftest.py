import random
import string

from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def browser() -> webdriver.Chrome:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def create_login(length=15, domain="@ya.ru"):
    domain_length = len(domain)
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(length - domain_length)]) + domain
