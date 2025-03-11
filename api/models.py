from django.db import models
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID
import uuid

class Persona(models.Model):
    """Model representing a person."""

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    id = models.AutoField(primary_key=True)
    
    nombre = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a name"
    )

    apellido = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a last name"
    )

    email = models.EmailField(
        unique=True,
        help_text="Enter an email"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    class Meta:
        # """id order"""
        # db_table = 'api_persona'
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['id'],
        #         name='unique_person_id',
        #         violation_error_message="Id already exists"
        #     ),
        # ]

        ordering = ['id']
