from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book


class BookTestCase(APITestCase):
    def setUp(self):
        self.book1 = Book.objects.create(
            title="One",
            author="AB C",
            publish_date="2000-12-30",
            isbn=9783161484102,
            price=10.68,
        )
        self.book2 = Book.objects.create(
            title="Two",
            author="CB A",
            publish_date="2005-01-01",
            isbn=1234567898765,
            price=10.69,
        )

    def test_books_has_authors(self):
        """Books are correctly saved"""
        book1 = Book.objects.get(title="One")
        book2 = Book.objects.get(title="Two")
        self.assertEqual(book1.author, self.book1.author)
        self.assertEqual(book2.author, self.book2.author)

    def test_get_book_successful(self):
        url = f"/api/v1/books/{self.book2._id}"
        response = self.client.get(url, format="json")
        self.assertEqual(response.json()["_id"], str(self.book2._id))
        self.assertEqual(response.json()["title"], self.book2.title)
