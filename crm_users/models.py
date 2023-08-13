from django.db import models
from django.conf import settings

from datetime import datetime

class User(models.Model):
    user_assoc = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    user_created = models.IntegerField(blank=True, default=0)
    contact_number = models.CharField(max_length=255, blank=True, default=None)
    street_name = models.CharField(max_length=255, blank=True, default=None)
    building_number = models.CharField(max_length=255, blank=True, default=None)
    city = models.CharField(max_length=255, blank=True, default=None)
    postcode = models.CharField(max_length=255, blank=True, default=None)
    date_updated = models.DateTimeField(default=datetime.now, blank=True)