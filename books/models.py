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

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title


