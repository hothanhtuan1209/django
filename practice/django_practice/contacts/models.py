from django.db import models
from django.core.validators import RegexValidator

from employees.models import Employee
from django_practice.models import BaseModel


class Contact(BaseModel):
    """
    A class representing different contact within the system.

    Attributes:
        id (UUIDField): The primary key for the contact.
        phone_number (CharField): The employee's phone number.
        address (CharField): The employee's address.
        employee (ForeignKey): The instance of employee whom the
        contact belongs.
        create_at (DateTimeField): A field to store the creation time of
        objects.
    """

    phone_number = models.CharField(
        validators=[RegexValidator(r"^0\d{9}$")], max_length=10
    )
    address = models.CharField(max_length=100)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE
    )
