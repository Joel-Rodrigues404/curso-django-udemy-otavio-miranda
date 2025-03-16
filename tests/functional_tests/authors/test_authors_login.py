import pytest
from .base import AuthorsBaseTest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    @pytest.mark.on_focus
    def test_user_valid_data_can_login_sucessfully(self):
        string_password = "password"

        user = User.objects.create_user(
            username='my_user',
            password=string_password
        )
        # Usuario abre a página de login

        self.browser.get(self.live_server_url + reverse('authors:login'))

        # Usuario ve o formulário de login

        form = self.browser.find_element(By.CLASS_NAME, 'main-form')  # noqa

        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        # Usuario digita user e senha

        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # Usuario envia o formulario
        form.submit()

        # Usuario ve a mensagem de login com seu nome

        self.sleep(1)
        self.assertIn(
            f"Your are logged in with {user.username}.",
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
        # End test
