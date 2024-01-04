import uuid

from django.db import models
from enum import Enum
from datetime import date, timedelta

from departments.models import Department
from django_practice.models import BaseModel


class ActiveStatus(Enum):
    ACTIVE = "Active"
    DISABLED = "Disabled"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Employee(BaseModel):
    """
    A class representing different employees within the system.

    Attributes:
        id (UUIDField): The primary key for the employee.
        first_name (CharField): The first name of the employee.
        last_name (CharField): The last name of the employee.
        gender (CharField): The gender of the employee.
        birthday (DateField): The employee's birth date.
        email(EmailField): The employee's email.
        status (CharField): The status of the employee in company.
        department (ForeignKey): This is the instance of department.
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    email = models.EmailField(max_length=100, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(
        max_length=10,
        choices=[(gender.value, gender.value) for gender in Gender],
        default=Gender.MALE.value,
    )
    status = models.CharField(
        max_length=10,
        choices=[(status.value, status.value) for status in ActiveStatus],
        default=ActiveStatus.ACTIVE.value,
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE
    )

    def get_full_name(self):
        """
        Combine first name and last name to create the full name of the
        employee.
        """

        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """
        Return a string representation of the Employee object.
        """

        return str(self.get_full_name())

    @classmethod
    def males_over_35(cls):
        """
        Get a list of all male employees older than 35 years old.
        """

        return cls.objects.filter(
            gender=Gender.MALE.value, birthday__lt=date.today() - timedelta(days=35 * 365)
        )

    @classmethod
    def sale_after_2000(cls):
        """
        Get a list of employees in the Sales department and born after 2000.
        """

        return cls.objects.filter(department__name='Sale', birthday__year__gt=2000)
