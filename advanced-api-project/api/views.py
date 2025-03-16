from django.shortcuts import render
from rest_framework import generics, permissions
from api.models import Book
from api.serializers import BookSerializer

# Create your views here.
class BookListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all books and creating a new book.
    Read access is open to everyone, but only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return []

#  Retrieve, Update, Delete Views
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single book.
    Read access is open to everyone, but only authenticated users can update/delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return []