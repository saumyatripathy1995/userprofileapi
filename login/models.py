from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    dob=models.DateField(max_length=50)
    emails=models.CharField(max_length=200)
    adress=models.CharField(max_length=400)