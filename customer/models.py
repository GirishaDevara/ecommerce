from django.db import models
from django.contrib.auth.models import User


class CustomerDefaultAddress(models.Model):
    Country_choices = (('india', 'India'),
                       ('USA','USA'))
    user = models.OneToOneField(User, related_name='UserProfiles', on_delete=models.CASCADE)
    name = models.CharField("Full name", max_length=1024)
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)
    city = models.CharField("City", max_length=1024)
    country = models.CharField("Country", max_length=20, choices=Country_choices)
    default = 0
