from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized


class AuthorsRegisterFormUnitTest(TestCase):

    @parameterized.expand([
        ("username", "Your username"),
        ("email", "Your E-mail"),
        ("first_name", "Ex.: Jonh"),
        ("last_name", "Ex.: Doe"),
        ("password", "Type your password"),
        ("password2", "Repeat your password"),
    ])
    def test_first_name_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs["placeholder"]
        self.assertEqual(placeholder, current_placeholder)
