from django.core.management.base import BaseCommand
from departments.models import Department


class Command(BaseCommand):
    help = 'Create initial departments'

    def handle(self, *args, **options):
        departments_data = [
            {'name': 'Accounting', 'description': 'Accounting department'}
        ]

        for data in departments_data:
            Department.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS('Initial departments created successfully!')
            )
