from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("doctor", "Doctor"),
        ("paciente", "Paciente"),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
