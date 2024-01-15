from datetime import date
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


def validate_age(birthday):
    age_limit = 18
    if relativedelta(date.today(), birthday).years < age_limit:
        raise ValidationError("Employee must be at least 18 years old")


def validate_email(email):
    if not email or "@" not in email:
        raise ValidationError("Invalid email format")
