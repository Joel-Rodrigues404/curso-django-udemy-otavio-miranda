from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': "First name",
            'last_name': "Last name",
            'username': "Username",
            'email': "E-mail",
            'password': "Password",
        }

        help_texts = {
            'email': 'The E-mail must be valid.',
        }
