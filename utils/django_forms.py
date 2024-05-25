from django.core.exceptions import ValidationError
import re


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, "")
    field.widget.attrs[attr_name] = f"{existing_attr} {attr_new_val}".strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, "placeholder", placeholder_val)


def strong_password(password):
    regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$")

    if not regex.match(password):
        raise ValidationError(
            (
                "password must heave at least one uppercase letter, "
                "one lower case letter and one number. The length should be "
                "at 8 characters."
            ),
            code="invalid",
        )
