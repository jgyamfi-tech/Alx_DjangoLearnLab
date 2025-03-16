from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Book, Author

# Create your tests here.
class BookTestCase(TestCase):
    def setUp(self):
        """Set up initial test data"""
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book", publication_year=2024, author=self.author
        )

    def test_book_creation(self):
        """Test that a book is created successfully"""
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(self.book.title, "Test Book")
