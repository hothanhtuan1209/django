from datetime import date
from dateutil.relativedelta import relativedelta


def calculate_age(age):
    """
    Calculate the age based on the provided birthday.
    """
    today = date.today()
    male_age = today - relativedelta(years=age)

    return male_age
