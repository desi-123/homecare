from django.db import models
from datetime import datetime

class ContactByMessage(models.Model):
 first_name = models.CharField(max_length=200)
 last_name = models.CharField(max_length=200)
 email = models.CharField(max_length=100)
 phone = models.CharField(max_length=100)
 message = models.TextField(blank=True)
 contact_date = models.DateTimeField(default=datetime.now, blank=True)
 user_id = models.IntegerField(blank=True)
 def __str__(self):
  return self.first_name