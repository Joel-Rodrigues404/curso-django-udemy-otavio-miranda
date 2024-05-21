from django.test import TestCase as DjangoTestCase
from unittest import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.urls import reverse


class AuthorsRegisterFormUnitTest(TestCase):

    @parameterized.expand(
        [
            ("username", "Your username"),
            ("email", "Your E-mail"),
            ("first_name", "Ex.: Jonh"),
            ("last_name", "Ex.: Doe"),
            ("password", "Type your password"),
            ("password2", "Repeat your password"),
        ]
    )
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs["placeholder"]
        self.assertEqual(placeholder, current_placeholder)

    @parameterized.expand(
        [
            (
                "username",
                (
                    "Username must have letters, numbers or one of those @.+-_. "
                    "The length should be between 4 and 150 characters"
                ),
            ),
            ("email", "The E-mail must be valid."),
            (
                "password",
                (
                    "password must heave at least one uppercase letter, "
                    "one lower case letter and one number. The length should be "
                    "at 8 characters."
                ),
            ),
        ]
    )
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(needed, current)

    @parameterized.expand(
        [
            ("username", "Username"),
            ("email", "E-mail"),
            ("first_name", "First name"),
            ("last_name", "Last name"),
            ("password", "Password"),
            ("password2", "Password2"),
        ]
    )
    def test_fields_label(self, field, label):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, label)


class AuthorsRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs) -> None:
        self.form_data = {
            "username": "Username",
            "first_name": "First name",
            "last_name": "Last name",
            "email": "email@email.com",
            "password": "Abc1234@",
            "password2": "Abc1234@",
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand(
        [
            ("username", "This field must be empty."),
            ("first_name", "Write your first name"),
            ("last_name", "Write your last name"),
            ("password", "Password must not be empty"),
            ("password2", "Please, reapet your password"),
            ("email", "The E-mail is required"),
        ]
    )
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ""
        url = reverse("authors:create")
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.context["form"].errors.get(field))

    def test_username_field_min_length_should_be_4(self):
        self.form_data['username'] = "joe"
        url = reverse("authors:create")
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Username must have at least 4 characters'
        self.assertIn(msg, response.context["form"].errors.get('username'))

    def test_username_field_max_length_should_be_150(self):
        self.form_data['username'] = "j" * 151
        url = reverse("authors:create")
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Username must have less than 150 characters'
        self.assertIn(msg, response.context["form"].errors.get('username'))