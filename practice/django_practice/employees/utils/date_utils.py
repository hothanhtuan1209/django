from datetime import date
from dateutil.relativedelta import relativedelta


def find_date(age):
    """
    Calculate the birthdate based on the provided age.
    """
    today = date.today()
    male_age = today - relativedelta(years=age)

    return male_age
