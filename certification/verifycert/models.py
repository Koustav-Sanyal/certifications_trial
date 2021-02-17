from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator, MaxLengthValidator, URLValidator
from django.contrib.auth.models import User
from django.conf import settings
import os

class Year(models.Model):
    year = models.CharField(max_length=4,null=True)

    def __str__(self):
        return self.year

class Events(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50,null = True)
    date = models.DateField(null = True)
    image = models.ImageField(upload_to = 'certificates/', null=True,blank = True)

    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.year) + " " + self.name

class Certificate(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    certificate_number = models.CharField(max_length=50, null=True)
    link = models.URLField(max_length=200, null=True,blank = True)
    email = models.EmailField(max_length=256, null=True,blank = True)
    rank = models.IntegerField(default=4,null=True,blank = True)

    submitted_at = models.DateTimeField(auto_now_add=True ,null=True)
    updated_at = models.DateTimeField(auto_now=True ,null=True)

    def __str__(self):
        return self.certificate_number + " " + self.name