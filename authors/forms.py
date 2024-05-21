from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
import re


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(
            (
                "password must heave at least one uppercase letter, "
                "one lower case letter and one number. The length should be "
                "at 8 characters."
            ),
            code='invalid'
        )


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs['placeholder'] = 'Uasadfadf'

        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your E-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: Jonh')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_placeholder(self.fields['password'], 'Type your password')
        add_placeholder(self.fields['password2'], 'Repeat your password')

    username = forms.CharField(
        label='Username',
        error_messages={
            "required": "This field must be empty.",
            "min_length": 'Username must have at least 4 characters',
            "max_length": 'Username must have less than 150 characters',
        },
        help_text=(
            'Username must have letters, numbers or one of those @.+-_. '
            'The length should be between 4 and 150 characters'
        ),
        min_length=4, max_length=150,
    )

    first_name = forms.CharField(
        error_messages={'required': 'Write your first name'},
        required=True,
        label='First name'
    )

    last_name = forms.CharField(
        error_messages={'required': 'Write your last name'},
        required=True,
        label='Last name'
    )

    email = forms.EmailField(
        required=True,
        label='E-mail',
        error_messages={'required': 'The E-mail is required'},
        help_text='The E-mail must be valid.'
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={
            "required": "Password must not be empty"
        },
        help_text=(
            "password must heave at least one uppercase letter, "
            "one lower case letter and one number. The length should be "
            "at 8 characters."
        ),
        validators=[strong_password],
        label='Password'
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='Password2',
        error_messages={
            "required": "Please, reapet your password"
        },
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]

        # labels = {
        #     "first_name": "First name",
        #     "last_name": "Last name",
        #     "username": "Username",
        #     "email": "E-mail",
        # }

        # error_messages = {
        #     "username": {
        #         "required": "This field must be empty."
        #     }}

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ]
            })
