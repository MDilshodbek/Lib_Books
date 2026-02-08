from django.shortcuts import render
from django.views.generic import ListView
from .models import Books

class BookListView(ListView):
    model = Books
    template_name = 'books/book_list.html'
