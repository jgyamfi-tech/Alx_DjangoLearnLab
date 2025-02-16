# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the book using its title
book = Book.objects.get(title="1984")

# Print book details
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
# Expected output: Title: 1984, Author: George Orwell, Year: 1949
```
