from django.contrib import admin
from .models import Customer
from .models import Book
from .models import CustomerBook
from .models import Author

# Register your models here.

class CustomerBookInline(admin.TabularInline):
    model = CustomerBook
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    # filter_horizontal = ('books',)
    inlines = (CustomerBookInline,)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(CustomerBook)
