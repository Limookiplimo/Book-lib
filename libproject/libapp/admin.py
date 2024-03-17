from django.contrib import admin
from .models import Book, BookCopy, Patron, Checkout,Program

# Register your models here.
admin.site.register(Book)
admin.site.register(BookCopy)
admin.site.register(Patron)
admin.site.register(Checkout)
admin.site.register(Program)