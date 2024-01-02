from django.db import models


class BaseModel(models.Model):
    """
    A base model with a 'create_at' field to track the creation
    time of objects.
    """

    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
