import random

from faker import Faker
from django.core.management.base import BaseCommand

from employees.models import Employee
from departments.models import Department


class Command(BaseCommand):
    help = 'Create fake employees for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating fake employees...'))

        department_names = Department.objects.values_list('name', flat=True)

        employees = []

        for i in range(200):
            first_name = Faker().first_name()
            last_name = Faker().last_name()
            birthday = Faker().date_of_birth(minimum_age=20, maximum_age=60)
            email = Faker().email()
            gender = random.choice(['Male', 'Female'])
            status = 'Active'

            department_name = random.choice(department_names)

            department = Department.objects.get(name=department_name)

            employees.append(
                Employee(
                    first_name=first_name,
                    last_name=last_name,
                    birthday=birthday,
                    email=email,
                    gender=gender,
                    status=status,
                    department=department
                )
            )

        Employee.objects.bulk_create(employees)

        self.stdout.write(
            self.style.SUCCESS('Fake employees created successfully!')
        )
