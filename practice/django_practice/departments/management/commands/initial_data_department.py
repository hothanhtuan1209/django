from django.core.management.base import BaseCommand
from departments.models import Department


class Command(BaseCommand):
    help = "Create initial departments"

    def handle(self, *args, **options):
        departments_data = [
            {"name": "Accounting", "description": "Accounting department"},
            {"name": "IT", "description": "Information Technology"},
            {"name": "Sale", "description": "Sales Department"},
            {"name": "HR", "description": "Human Resources Department"},
            {"name": "Business", "description": "Business Department"},
        ]

        departments_to_create = [
            Department(name=data["name"], description=data["description"])
            for data in departments_data
        ]

        Department.objects.bulk_create(departments_to_create)

        self.stdout.write(
            self.style.SUCCESS("Initial departments created successfully!")
        )
