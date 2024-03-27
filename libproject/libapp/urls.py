from django.urls import path
from .views import books_library, inventory, acquisitions, checkouts, patrons, programs, suppliers, createsupplier, generate_po_number

urlpatterns = [
    path('library',books_library, name='library'),
    path('inventory',inventory, name='inventory'),
    path('acquisitions',acquisitions, name='acquisitions'),
    path('checkouts',checkouts, name='checkouts'),
    path('patrons',patrons, name='patrons'),
    path('programs',programs, name='programs'),
    path('suppliers',suppliers, name='suppliers'),
    path('createsupplier',createsupplier, name='createsupplier'),
    path('generateponum', generate_po_number, name='genetateponum'),
]
