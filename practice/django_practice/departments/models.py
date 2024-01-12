from django.db import models

from django_practice.models import BaseModel


class Department(BaseModel):
    """
    A class representing different departments within the system.

    Attributes:
        - id (UUID): The primary key for the department.
        - name (CharField): The name of the department.
        - description (TextField): The description of the department.
        - create_at (DateTimeField): A field to store the creation time of
        objects.
        - archived (BooleanField): A field to indicate whether the object is
        archived (deleted) or not.
        - modified_at (DateTimeField): A field to store the last modification
        time of objects.
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200)

    def __str__(self):
        """
        Return s string representation of the Department object.
        """

        return str(self.name)
