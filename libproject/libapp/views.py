from django.shortcuts import render
from django.http import JsonResponse
from .models import Book,Patron,Program

# Create your views here.
def books_library(request):
    books = Book.objects.all()
    context = {'books': list(books.values('title','author'))}
    return JsonResponse(context, safe=False)

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
            'description': description
        }
        
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
            'address': address,
        }
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
            'end_date': end_date,
        }
        Program.objects.create(**data)
        return JsonResponse({'message': 'Program created successfully'})
