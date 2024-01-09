import uuid
from django.db import models


class BaseModel(models.Model):
    """
    A base model with 'create_at' and 'id' fields to track the creation
    time and unique identifier of objects.

    Attributes:
        create_at (DateTimeField): A field to store the creation time of objects.
        id (UUIDField): A field to store a unique identifier (UUID) for each object.
    """

    create_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
