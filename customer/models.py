from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='UserProfiles', on_delete=models.CASCADE)
    address = models.
