import allure

from pages.home_page import HomePage
from helpers.email_generator import create_login
from data.user_data import *


class TestRegister:
    @allure.title("Зарегистрировать пользователя")
    def test_register_new_user(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.register_user(create_login(), registered_user.password)
        home_page.assert_user_is_registered()

    @allure.title("Войти в систему")
    def test_login_user(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.login_user(registered_user.email, registered_user.password)
        home_page.assert_user_is_registered()

    @allure.title("Выйти из системы")
    def test_logout_user(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.login_user(registered_user.email, registered_user.password)
        home_page.logout_user()
        home_page.assert_user_is_log_out()

    @allure.title("Разместить объявление не авторизованным пользователем.")
    def test_place_adw_by_not_auth_user(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_adw_btn()
        home_page.assert_login_modal_is_displayed()

    @allure.title("Регистрация пользователя с существующем email")
    def test_register_existing_user(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.register_user(registered_user.email, registered_user.password)
        home_page.assert_user_is_not_registered()

    @allure.title("Регистрация пользователя с некорректным email")
    def test_register_new_user_with_invalid_email(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.register_user(fake_user.email, fake_user.password)
        home_page.assert_user_is_not_registered()