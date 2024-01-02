import uuid
from django.db import models

from django_practice.models import BaseModel


class Department(BaseModel):
    """
    A class representing different departments within the system.

    Attributes:
        id (UUID): The primary key for the department
        name (CharField): The name of the department
        description (TextField): the description of the department
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200)

    def __str__(self):
        """
        Return s string representation of the Department object.
        """

        return str(self.name)
