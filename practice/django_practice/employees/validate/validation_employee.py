from datetime import date
from django.core.exceptions import ValidationError
from ..utils.number_of_age import calculate_age


def validate_age(birthday):
    age_limit = 18
    if calculate_age(date.today(), birthday) < age_limit:
        raise ValidationError("Employee must be at least 18 years old")


def validate_email(email):
    if not email or "@" not in email:
        raise ValidationError("Invalid email format")
