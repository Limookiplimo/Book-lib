from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import BookCopy, Book,Patron,Program, PurchaseOrder, Checkout, Patron, Supplier
from datetime import datetime


# Create your views here.
def books_library(request):
    books = BookCopy.objects.all()
    context = {'books': books}
    return render(request, 'libapp/home.html',context)

def inventory(request):
    books = BookCopy.objects.all()
    context = {'books': books}
    return render(request, 'libapp/inventory.html',context)

def patrons(request):
    patrons = Patron.objects.all()
    context = {'patrons':patrons}
    return render(request, 'libapp/patrons.html',context)

def acquisitions(request):
    purchase_orders = PurchaseOrder.objects.all()
    context = {'purchase_orders': purchase_orders}
    return render(request, 'libapp/acquisitions.html', context)

def checkouts(request):
    checkouts = Checkout.objects.all()
    context = {'checkouts': checkouts}
    return render(request, 'libapp/lending.html', context)

def programs(request):
    programs = Program.objects.all()
    context = {'programs': programs}
    return render(request, 'libapp/programs.html', context)

def suppliers(request):
    suppliers = Supplier.objects.all()
    context = {'suppliers': suppliers}
    return render(request, 'libapp/suppliers.html', context)

def createsupplier(request):
    sup_count = Supplier.objects.count()
    series_number = sup_count + 1
    sup_code = (f"SUP{series_number:003d}").upper()

    if request.method == 'POST':
        name = request.POST.get('name').upper()
        s_type = request.POST.get('s_type').upper()
        email = request.POST.get('email').lower()
        phone = request.POST.get('phone')
        address = request.POST.get('address').upper()

        data = {
            'sup_code': sup_code,
            'name': name,
            's_type': s_type,
            'email': email,
            'phone': phone,
            'address': address
        }
        Supplier.objects.create(**data)
        return redirect(suppliers)

def generate_po_number(request):
    po_num = (f"PO{datetime.now().strftime('%Y%m%d%H%M%S')}").upper()
    suburl = f"/create/purchaseorder/{po_num}"
    return redirect(suburl)

def create_purchase_order(request):
    if request.method == 'POST':
        pass

def acquire_books(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        publication_date = request.POST.get('publication_date')
        publisher = request.POST.get('publisher')
        description = request.POST.get('description')  
        data = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'publication_date': publication_date,
            'publisher': publisher,
            'description': description}
        Book.objects.create(**data)
        return JsonResponse({'message': 'Book created successfully'})

def register_patron(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number,
            'address': address}
        Patron.objects.create(**data)
        return JsonResponse({'message': 'Patron created successfully'})

def create_program(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        data = {
            'name': name,
            'description': description,
            'start_date': start_date,
            'end_date': end_date}
        Program.objects.create(**data)
        return JsonResponse({'message': 'Program created successfully'})

