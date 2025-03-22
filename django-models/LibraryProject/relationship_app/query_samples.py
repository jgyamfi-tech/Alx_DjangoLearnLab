import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return [book.title for book in books]

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return [book.title for book in books]

# Retrieve the librarian for a library
def get_librarian(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian.name if library.librarian else "No librarian assigned"

# Example usage
if __name__ == "__main__":
    print("Books by J.K. Rowling:", books_by_author("J.K. Rowling"))
    print("Books in Central Library:", books_in_library("Central Library"))
    print("Librarian of Central Library:", get_librarian("Central Library"))
