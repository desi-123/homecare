from django.db import models

class Question(models.Model):
 q1 = models.CharField(max_length=300)
 ans1 = models.TextField(blank=True)
 q2 = models.CharField(max_length=300)
 ans2 = models.TextField(blank=True)
 q3 = models.CharField(max_length=300)
 ans3 = models.TextField(blank=True)
 q4 = models.CharField(max_length=300)
 ans4 = models.TextField(blank=True)
 q5 = models.CharField(max_length=300)
 ans5 = models.TextField(blank=True)
 q6 = models.CharField(max_length=300)
 ans6 = models.TextField(blank=True)
 q7 = models.CharField(max_length=300)
 ans7 = models.TextField(blank=True)
 q8 = models.CharField(max_length=300)
 ans8 = models.TextField(blank=True)
 q9 = models.CharField(max_length=300)
 ans9 = models.TextField(blank=True)
 q10 = models.CharField(max_length=300)
 ans10 = models.TextField(blank=True)
 def __str__(self):
  return self.q1
