from datetime import date


def calculate_age(birthday):
    """
    Calculate the age based on the provided birthday.
    """

    today = date.today()
    calculated_age = today.year - birthday.year - (
        (today.month, today.day) < (birthday.month, birthday.day)
    )

    return calculated_age
