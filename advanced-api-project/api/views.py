from django.shortcuts import render
from rest_framework import generics, permissions
from api.models import Book
from api.serializers import BookSerializer


# Create your views here.

#  List all books & Create a new book
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Open to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

#  Retrieve, Update, and Delete a book
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves details of a single book by ID.
    Open to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]