from datetime import date
from dateutil.relativedelta import relativedelta


def find_date(age):
    """
    Calculate the age based on the provided birthday.
    """
    today = date.today()
    male_age = today - relativedelta(years=age)

    return male_age
