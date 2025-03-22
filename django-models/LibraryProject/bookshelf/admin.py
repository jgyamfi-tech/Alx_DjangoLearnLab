from django.contrib import admin
from .models import Book  # Import the Book model


# Custom admin class for Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in the admin list view
    list_filter = ('publication_year',)  # Add a filter for publication year
    search_fields = ('title', 'author')  # Enable search by title and author

# Register the Book model with custom admin settings
admin.site.register(Book, BookAdmin)