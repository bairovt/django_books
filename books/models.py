from django.db import models
from datetime import datetime

# Create your models here.

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


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, blank=True, null=True)
    phone2 = models.CharField(max_length=30, blank=True, null=True)
    # job
    jobname = models.CharField(max_length=255, blank=True, null=True)
    # place
    placename = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)

    books = models.ManyToManyField(Book, through='CustomerBook')

    def __str__(self):
        return self.name


class CustomerBook(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, blank=True, null=True) # ordered, refused
    received_at = models.DateField(null=True, blank=True)
    paidSum = models.PositiveIntegerField(blank=True, null=True)