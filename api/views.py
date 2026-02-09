from django.shortcuts import render
from rest_framework.generics import ListAPIView

from books.models import Books
from .serializers import BooksSerializer 

# Create your views here.
class BooksAPIView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer