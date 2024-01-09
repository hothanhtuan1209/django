from django.db import models
from django.core.exceptions import ValidationError

from departments.models import Department
from django_practice.models import BaseModel
from django_practice.constants.enum import Gender, ActiveStatus
from number_of_age import calculate_age


class EmployeeFilterManager(models.Manager):
    def get_employees_filtered_by_age(self):
        """
        Get all employee have birthday greater than 20 years old
        """

        return self.filter(calculate_age(Employee.birthday) > 20)


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
    birthday = models.DateField()
    email = models.EmailField(max_length=100, unique=True)
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

    def validate_data(self):
        super(Employee, self).clean()

        age_limit = 18
        if calculate_age(self.birthday) < age_limit:
            raise ValidationError("Employee must be at least 20 years old")

        if not self.email or "@" not in self.email:
            raise ValidationError("Invalid email format")

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

        return cls.objects.filter(gender=Gender.MALE.value).filter(
            calculate_age(Employee.birthday) > 35
        )

    @classmethod
    def sale_after_2000(cls):
        """
        Get a list of employees in the Sales department and born after 2000.
        """

        return cls.objects.filter(department__name="Sale", birthday__year__gt=2000)

    @classmethod
    def get_it_employees(cls):
        """
        Return queryset contain a list employee in IT department.
        """
        return cls.objects.filter(department__name="IT")
