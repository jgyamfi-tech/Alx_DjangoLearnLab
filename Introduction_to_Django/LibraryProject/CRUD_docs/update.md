# Update Operation

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the book title
book.title = "Nineteen Eighty-Four"
book.save()  # Save changes to the database

# Verify the update
updated_book = Book.objects.get(id=book.id)  # Retrieve again
print(f"Updated Title: {updated_book.title}")
# Expected output: Updated Title: Nineteen Eighty-Four
```
