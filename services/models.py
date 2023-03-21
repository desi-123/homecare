from django.db import models

class Service_text(models.Model):
 title = models.CharField(max_length=200)
 description = models.TextField(blank=True)
 btn = models.CharField(max_length=100, blank=True)
 subtitle = models.CharField(max_length=300)
 phone = models.CharField(max_length=100)
 def __str__(self):
  return self.title

class Service_photos(models.Model):
 title = models.CharField(max_length=200)
 description = models.TextField(blank=True)
 photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
 photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
 photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
 photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
 is_published = models.BooleanField(default=True)
 def __str__(self):
  return self.title

class Service_list(models.Model):
 title = models.CharField(max_length=200)
 description = models.TextField(blank=True)
 def __str__(self):
  return self.title


