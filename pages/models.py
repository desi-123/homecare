from django.db import models

class About(models.Model):
 title = models.CharField(max_length=200)
 description_one = models.TextField(blank=True)
 description_two = models.TextField(blank=True)
 name = models.CharField(max_length=200)
 photo_about = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
 job = models.CharField(max_length=200)
 profile_description = models.TextField(blank=True)
 def __str__(self):
  return self.title

class About_team(models.Model):
 title = models.CharField(max_length=200)
 description = models.TextField(blank=True)
 name = models.CharField(max_length=200)
 photo_team = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
 def __str__(self):
  return self.title

class Home(models.Model):
 title = models.CharField(max_length=200)
 description_one = models.TextField(blank=True)
 description_two = models.TextField(blank=True)
 description_three = models.TextField(blank=True)
 subtitle = models.CharField(max_length=200)
 description_four = models.TextField(blank=True)
 url_text = models.CharField(max_length=100)
 def __str__(self):
  return self.title


class Contact(models.Model):
 email = models.EmailField(max_length=100, blank=True)
 phone = models.CharField(max_length=100)
 description_one = models.TextField(blank=True)
 description_two = models.TextField(blank=True)
 description_three = models.TextField(blank=True)
 address = models.CharField(max_length=200)
 city = models.CharField(max_length=100)
 state = models.CharField(max_length=100)
 zipcode = models.CharField(max_length=20)

 def __str__(self):
  return self.state


