
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from app.users.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self) -> str:
        return reverse('users:detail', kwargs={'pk': self.id})
