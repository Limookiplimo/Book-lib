from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    class Meta:
        db_table = "books"

class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    status = models.CharField(max_length=20, choices=(
        ('available', 'Available'),
        ('checked_out', 'Checked Out'),
        ('lost', 'Lost'),
        ('damaged', 'Damaged')
    ))
    due_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.book.title} (Copy)"
    
    class Meta:
        db_table = "bookcopy"

class Patron(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = "patrons"

class Checkout(models.Model):
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE, related_name='checkouts')
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE, related_name='checkouts')
    checkout_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.patron.first_name} {self.patron.last_name} - {self.book_copy.book.title}"
    
    class Meta:
        db_table = "checkout"

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "program"