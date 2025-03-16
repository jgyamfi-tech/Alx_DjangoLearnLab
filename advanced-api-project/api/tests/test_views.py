from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        """Set up test data for the API"""
        self.client = APIClient()

        # Create test author
        self.author = Author.objects.create(name="John Doe")

        # Create test book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2023,
            author=self.author
        )

        self.book_url = f"/api/books/{self.book.id}/"

    def test_get_all_books(self):
        """Test retrieving a list of books"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_book(self):
        """Test retrieving a single book by ID"""
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_create_book(self):
        """Test creating a new book"""
        new_book_data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post("/api/books/", new_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        """Test updating a book"""
        update_data = {"title": "Updated Book"}
        response = self.client.patch(self.book_url, update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get("/api/books/?search=Test Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_ordering_books(self):
        """Test ordering books by publication year"""
        response = self.client.get("/api/books/?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
