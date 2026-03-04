from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        RESIDENT = 'resident', 'Resident'
        SECURITY = 'security', 'Security'
        ASSOCIATION_STAFF = 'association_staff', 'Association Staff'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(max_length=32, choices=Role.choices, default=Role.RESIDENT)
    phone_number = models.CharField(max_length=20, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username} ({self.role})'
