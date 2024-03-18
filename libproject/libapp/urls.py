from django.urls import path
from .views import books_library, acquisitions, checkouts, patrons, programs, suppliers, createsupplier

urlpatterns = [
    path('library',books_library, name='library'),
    path('acquisitions',acquisitions, name='acquisitions'),
    path('checkouts',checkouts, name='checkouts'),
    path('patrons',patrons, name='patrons'),
    path('programs',programs, name='programs'),
    path('suppliers',suppliers, name='suppliers'),
    path('createsupplier',createsupplier, name='createsupplier'),
]
