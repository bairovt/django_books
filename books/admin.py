from django.contrib import admin
from .models import Customer
from .models import Book
from .models import Author

# Register your models here.

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Author)
