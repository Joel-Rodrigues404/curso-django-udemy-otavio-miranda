from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import AuthorsBaseTest
import pytest


@pytest.mark.functional_test
class AuthorsRegisterTest(AuthorsBaseTest):
    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(
            By.XPATH, f'//input[@placeholder="{placeholder}"]'
        )

    def fill_form_dummy_data(self, form):
        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form'
        )

    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register/')

        form = self.get_form()

        self.fill_form_dummy_data(form)

        email_field = form.find_element(By.NAME, 'email')
        email_field.clear()
        email_field.send_keys('dummy@email.com')

        callback(form)
        return form

    def test_empty_first_name_error_message(self):
        def callback(form):
            first_name_field = self.get_by_placeholder(form, 'Ex.: Jonh')
            first_name_field.send_keys(' ')
            first_name_field.send_keys(Keys.ENTER)

            self.sleep(1)

            form = self.get_form()

            self.assertIn("Write your first name", form.text)
        self.form_field_test_with_callback(callback)

    def test_empty_last_name_error_message(self):
        def callback(form):
            last_name_field = self.get_by_placeholder(form, 'Ex.: Doe')
            last_name_field.send_keys(' ')
            last_name_field.send_keys(Keys.ENTER)

            self.sleep(1)

            form = self.get_form()

            self.assertIn("Write your last name", form.text)
        self.form_field_test_with_callback(callback)

    def test_empty_username_error_message(self):
        def callback(form):
            username_field = self.get_by_placeholder(form, 'Your username')
            username_field.send_keys(' ')
            username_field.send_keys(Keys.ENTER)

            self.sleep(1)

            form = self.get_form()

            self.assertIn("This field must be empty.", form.text)
        self.form_field_test_with_callback(callback)

    def test_invalid_email_error_message(self):
        def callback(form):
            email_field = self.get_by_placeholder(form, 'Your E-mail')
            email_field.clear()
            email_field.send_keys('email@invalid')
            email_field.send_keys(Keys.ENTER)

            self.sleep(1)

            form = self.get_form()

            self.assertIn("The E-mail must be valid.", form.text)
        self.form_field_test_with_callback(callback)

    def test_password_do_not_match(self):
        def callback(form):
            password1_field = self.get_by_placeholder(
                form, 'Type your password'
            )
            password2_field = self.get_by_placeholder(
                form, 'Repeat your password'
            )

            password1_field.send_keys('P@sswor0d')
            password2_field.send_keys('P@sswor0d_different')

            password2_field.send_keys(Keys.ENTER)

            self.sleep(1)

            form = self.get_form()

            self.assertIn("Password and password2 must be equal", form.text)
        self.form_field_test_with_callback(callback)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.get_by_placeholder(form, 'Ex.: Jonh').send_keys('first name')
        self.get_by_placeholder(form, 'Ex.: Doe').send_keys('last name')
        self.get_by_placeholder(form, 'Your username').send_keys('username')
        self.get_by_placeholder(form, 'Your E-mail').send_keys('example@email.com')  # noqa
        self.get_by_placeholder(form, 'Type your password').send_keys('P@sswor0d')   # noqa
        self.get_by_placeholder(form, 'Repeat your password').send_keys('P@sswor0d')  # noqa

        form.submit()

        self.sleep(1)

        self.assertIn(
            "Your user is created, please log in.",
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
