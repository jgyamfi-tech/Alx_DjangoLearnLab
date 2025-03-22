from django.test import TestCase
from django.conf import settings
from django.apps import apps
from rest_framework import serializers
from api.models import Author, Book
from api.serializers import BookSerializer, AuthorSerializer

class ProjectSetupTests(TestCase):

    def test_django_installed(self):
        """Check if Django is installed and settings are configured."""
        self.assertTrue(settings.configured, "Django settings are not configured properly.")

    def test_api_app_installed(self):
        """Check if 'api' app is installed."""
        self.assertTrue(apps.is_installed('api'), "The 'api' app is not installed.")

    def test_rest_framework_installed(self):
        """Check if Django REST Framework is in INSTALLED_APPS."""
        self.assertIn('rest_framework', settings.INSTALLED_APPS, "Django REST Framework is not added to INSTALLED_APPS.")

    def test_models_exist(self):
        """Check if Author and Book models exist."""
        self.assertTrue(hasattr(Author, '_meta'), "Author model is missing.")
        self.assertTrue(hasattr(Book, '_meta'), "Book model is missing.")

    def test_models_fields(self):
        """Check if Author and Book models have the required fields."""
        author_fields = [field.name for field in Author._meta.fields]
        book_fields = [field.name for field in Book._meta.fields]

        self.assertIn('name', author_fields, "Author model is missing the 'name' field.")
        self.assertIn('title', book_fields, "Book model is missing the 'title' field.")
        self.assertIn('publication_year', book_fields, "Book model is missing the 'publication_year' field.")
        self.assertIn('author', book_fields, "Book model is missing the 'author' field.")

    def test_book_serializer(self):
        """Check if BookSerializer is implemented correctly."""
        self.assertTrue(issubclass(BookSerializer, serializers.ModelSerializer), "BookSerializer is not a subclass of ModelSerializer.")

    def test_author_serializer(self):
        """Check if AuthorSerializer is implemented correctly."""
        self.assertTrue(issubclass(AuthorSerializer, serializers.ModelSerializer), "AuthorSerializer is not a subclass of ModelSerializer.")
        self.assertIn('books', AuthorSerializer.Meta.fields, "AuthorSerializer is missing the 'books' field.")
