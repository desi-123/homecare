from django.db import models
from datetime import datetime

# Create your models here.
class Testimonials(models.Model):
 title = models.CharField(max_length=300, blank=True) 
 description = models.TextField(blank=True)
 subtitle = models.CharField(max_length=900)
 body = models.TextField(blank=True)
 is_published = models.BooleanField(default=True)
 post_date = models.DateField(default=datetime.now, blank=True)
 def __str__(self):
  return self.title + '|' + str(self.post_date)