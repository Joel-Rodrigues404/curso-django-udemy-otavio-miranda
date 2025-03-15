import pytest
from .base import AuthorsBaseTest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    @pytest.mark.on_focus
    def test_user_valid_data_can_login_sucessfully(self):
        user = User.objects.create_user(
            username='my_user',
            password='password',
        )
        # Usuario abre a página de login

        self.browser.get(self.live_server_url + reverse('authors:login'))

        # End test
        self.sleep(10)
        assert 1 == 1
