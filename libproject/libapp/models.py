from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    edition = models.CharField(max_length=20,null=True)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    class Meta:
        db_table = "book"

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
    id_num = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = "patron"

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

class Supplier(models.Model):
    sup_code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    s_type = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        db_table = "supplier"

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at =  models.DateTimeField(auto_now=True)
    issued_at =  models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']
        db_table = "purchase_order"

class POItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    edition = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "po_item"

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.title} (${self.subtotal})"
