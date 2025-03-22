from django.shortcuts import render
from .models import Book  # Import the Book model
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Library Project</h1>")

def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, "list_books.html", {"books": books})  # Pass books to the template

# Create your views here.
from django.views.generic import DetailView
from .models import Library  # Import the Library model

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"  # Uses the library_detail.html template
    context_object_name = "library"  # The variable used in the template to access the Library object

