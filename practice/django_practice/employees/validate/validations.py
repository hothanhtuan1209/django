from datetime import date
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


def validate_age(birthday):
    age_limit = 18
    if relativedelta(date.today(), birthday).years < age_limit:
        raise ValidationError("Employee must be at least 18 years old")


def validate_name(text):
    words = text.split()
    for word in words:
        if not word[0].isupper():
            raise ValidationError("The first letter of a word must be capitalized")
