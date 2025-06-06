from pages.home_page import HomePage


class TestCreateListing:
    def test_create_adw(self, browser, create_login):
        home_page = HomePage(browser)
        home_page.open_home_page()
        home_page.click_on_login_and_register_btn()
        home_page.register_user(create_login, "qwerty123")
        home_page.assert_user_is_registered()
        create_listing_page = home_page.click_on_adw_btn()
        create_listing_page.create_adw("Test", "Книги", "Казань", "Описание", 999)
        home_page.assert_is_home_page()
        profile_page = home_page.click_on_profile_logo()
        profile_page.assert_listing_cards_is_visible()