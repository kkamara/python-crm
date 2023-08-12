from django.db import models
from django.conf import settings

from datetime import datetime

class User(models.Model):
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, unique=True)
    contact_number = models.CharField(max_length=255, blank=True)
    street_name = models.CharField(max_length=255, blank=True)
    building_number = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=255, blank=True)
    date_updated = models.DateTimeField(default=datetime.now, blank=True)