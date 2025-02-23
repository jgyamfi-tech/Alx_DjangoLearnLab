# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
book.delete()

# Confirm deletion by checking if any books exist
books = Book.objects.all()
print(list(books))  
# Expected output: []
```
