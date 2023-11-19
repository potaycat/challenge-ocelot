from django.test import TestCase
from .models import Book


class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(
            title="One",
            author="AB C",
            publish_date="2000-12-30",
            isbn=9783161484102,
            price=10.68,
        )
        Book.objects.create(
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
        self.assertEqual(book1.author, "AB C")
        self.assertEqual(book2.author, "CB A")
