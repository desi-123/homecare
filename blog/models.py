from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Blog(models.Model):
 title = models.CharField(max_length=300) 
 title_tag = models.CharField(max_length=250, default='Blog')
 author = models.ForeignKey(User, on_delete=models.CASCADE)
 body = models.TextField()
 is_published = models.BooleanField(default=True)
 post_date = models.DateField(default=datetime.now, blank=True)
 def __str__(self):
  return self.title + '|' + str(self.author)