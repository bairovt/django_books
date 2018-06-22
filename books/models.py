from django.db import models
from datetime import datetime

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    phone2 = models.CharField(max_length=30)
    # job
    jobname = models.CharField(max_length=255)
    # place
    placename = models.CharField(max_length=255)
    
    note = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)


# class Book(models)