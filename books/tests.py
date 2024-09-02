from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book

class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "title": "Python info",
            "author": "Guido van rassum ",
            "published_date": "1991-02-20",
            "isbn": "9780743273565",
            "page_count": 180,
            "cover": "https://www.python.org/",
            "language": "English"
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        response = self.client.post(reverse('book-create'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_book(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        updated_data = self.book_data.copy()
        updated_data['title'] = "The Great Gatsby Updated"
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)