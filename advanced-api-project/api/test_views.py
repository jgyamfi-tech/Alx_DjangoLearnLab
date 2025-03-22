from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Book, Author  # Ensure Author model is imported


class BookAPITestCase(APITestCase):
    def setUp(self):
        """Setup test data"""
        # Create a test user and authentication token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Set authentication for the client
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create a test author
        self.author = Author.objects.create(name="Test Author")

        # Create a test book
        self.book = Book.objects.create(title="Test Book", author=self.author, publication_year=2024)

    def test_create_book(self):
        """Test creating a new book"""
        data = {
            "title": "New Book",
            "author": self.author.id,  # Use author ID instead of name
            "publication_year": 2025
        }

        response = self.client.post("/api/books/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_update_book(self):
        """Test updating a book"""
        data = {
            "title": "Updated Book",
            "author": self.author.id,
            "publication_year": 2025
        }

        response = self.client.put(f"/api/books/{self.book.id}/", data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)