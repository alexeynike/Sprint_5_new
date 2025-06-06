from pages.home_page import HomePage

class TestRegister:
    def test_register_new_user(self, browser, create_login):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.register_user(create_login, "qwerty123")
        home_page.assert_user_is_registered()

    def test_register_existing_user(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.register_user("test123@test.ru", "qwerty123")
        home_page.assert_user_is_not_registered()

    def test_register_new_user_with_invalid_email(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.register_user("test123test.ru", "qwerty123")
        home_page.assert_user_is_not_registered()


    def test_login_user(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.login_user("test123@test.ru", "123456")
        home_page.assert_user_is_registered()

    def test_logout_user(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.login_user("test123@test.ru", "123456")
        home_page.logout_user()
        home_page.assert_user_is_log_out()

    def test_place_adw_by_not_auth_user(self, browser):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_adw_btn()
        home_page.assert_login_modal_is_displayed()
