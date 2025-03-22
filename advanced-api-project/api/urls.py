from django.urls import path
from api.views import BookListCreateView, BookDetailView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),  # Supports GET & POST
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Supports GET, PUT, DELETE
]

