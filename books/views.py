from django.shortcuts import render

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

from rest_framework.exceptions import NotFound

class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        try:
            return super().get_object()
        except:
            raise NotFound("Book not found")

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['author', 'published_date', 'language']