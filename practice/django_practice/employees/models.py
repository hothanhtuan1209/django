from django.db import models
from datetime import date

from departments.models import Department
from django_practice.models import BaseModel
from django_practice.constants.enum import Gender, ActiveStatus
from .utils.number_of_age import calculate_age
from .validate.validation_employee import validate_age, validate_email


class EmployeeQuerySet(models.QuerySet):
    def males_over_age(self):
        """
        Get a list of all male employees older than 35 years old.
        """

        today = date.today()
        age_variable = 35

        employees_over_age = [
            employee
            for employee in self.filter(gender=Gender.MALE.value)
            if calculate_age(today, employee.birthday) > age_variable
        ]

        return employees_over_age

    def sale_after_year(self):
        """
        Get a list of employees in the Sales department and born after 2000.
        """

        year_of_birth = 2000
        return self.filter(
            department__name="Sale", birthday__year__gt=year_of_birth
        )

    def get_it_employees(self):
        """
        Return queryset contain a list employee in IT department.
        """

        return self.filter(department__name="IT")


class EmployeeFilterManager(models.Manager):
    def get_employees_filtered_by_age(self):
        """
        Get all employee have birthday greater than 20 years old
        """

        today = date.today()
        age_limit = 20

        employees_over_20 = []

        for employee in self.filter():
            age = calculate_age(today, employee.birthday)
            if age > age_limit:
                employees_over_20.append(employee)

        return employees_over_20


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
        create_at (DateTimeField): A field to store the creation time of
        objects.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(validators=[validate_age])
    email = models.EmailField(max_length=100, unique=True, validators=[validate_email])
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
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    objects = EmployeeFilterManager()

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
