from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    joining_data = models.DateTimeField(auto_now=True)

    bio = models.TextField(blank=True, null=True)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.username