import allure

from utils.actions.base_page_actions import BasePageActions
from utils.page_objects.login_page import LoginPagePageObject


class LoginPageActions(BasePageActions):
    def __init__(self, driver, config):
        super().__init__(driver, config)

    @allure.step("Check login form elements")
    def check_login_form_elements(self):
        self.is_element_visible(LoginPagePageObject.login_form)

        self.is_element_visible(LoginPagePageObject.back_button)
        self.is_element_visible(LoginPagePageObject.ya_id_logo)
        self.is_element_visible(LoginPagePageObject.login_form_title)

        self.is_element_visible(LoginPagePageObject.login_by_email_button)
        self.is_element_visible(LoginPagePageObject.login_by_phone_button)

        self.is_element_visible(LoginPagePageObject.email_input)

        self.is_element_visible(LoginPagePageObject.sign_in_button)
        self.is_element_visible(LoginPagePageObject.create_id_button)

        self.is_element_visible(LoginPagePageObject.auth_social_title)
        self.is_element_visible(LoginPagePageObject.auth_by_vk_button)
        self.is_element_visible(LoginPagePageObject.auth_by_gg_button)
        self.is_element_visible(LoginPagePageObject.auth_by_qr_button)
        self.is_element_visible(LoginPagePageObject.auth_by_fb_button)
        self.is_element_visible(LoginPagePageObject.auth_social_more_button)

    @allure.step("Check auth url in new window")
    def check_auth_url_in_new_window(self, expected_url):
        self.switch_to_new_window()
        self.check_url(expected_url)
        self.close_current_window()
        self.switch_to_new_window()
