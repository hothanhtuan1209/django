from django.core.management.base import BaseCommand
from employees.models import Employee
from datetime import datetime
from departments.models import Department


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Get existing departments
        it_department = Department.objects.get(name='IT')
        hr_department = Department.objects.get(name='HR')
        sales_department = Department.objects.get(name='Sale')

        # Create employees and link them to existing departments
        Employee.objects.get_or_create(
            first_name='Tran Van',
            last_name='Son',
            birthday=datetime(1990, 7, 17),
            email='sontran1707@gmail.com',
            gender='Male',
            status='Active',
            department=it_department
        )

        Employee.objects.get_or_create(
            first_name='Tran Thi',
            last_name='No',
            birthday=datetime(2000, 8, 22),
            email='nothi@gmail.com',
            gender='Female',
            status='Active',
            department=hr_department
        )

        Employee.objects.get_or_create(
            first_name='Nguyen Van',
            last_name='Nhat',
            birthday=datetime(1999, 11, 10),
            email='nhatnguyen@gmail.com',
            gender='Male',
            status='Active',
            department=sales_department
        )

        self.stdout.write(
            self.style.SUCCESS('Initial data created successfully!')
        )
