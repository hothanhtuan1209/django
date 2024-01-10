from datetime import date
from django.core.exceptions import ValidationError
from ..utils.number_of_age import calculate_age


def validate_age(employee):
    age_limit = 18
    if calculate_age(date.today(), employee.birthday) < age_limit:
        raise ValidationError("Employee must be at least 18 years old")


def validate_email(employee):
    if not employee.email or "@" not in employee.email:
        raise ValidationError("Invalid email format")
