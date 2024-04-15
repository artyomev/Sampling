from django.db import models
from django.contrib.auth.models import AbstractUser


class MusUser(AbstractUser):
    position = models.TextField(blank=False)
    business_unit = models.TextField(blank=False)

