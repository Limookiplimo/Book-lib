from django.urls import path
from .views import books_library

urlpatterns = [
    path('',books_library, name='library'),
]
