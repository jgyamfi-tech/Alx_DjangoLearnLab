from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for listing books using ListAPIView (optional, can be removed if not needed)
    path('books/', BookList.as_view(), name='book-list'),

    # Register ViewSet routes
    path('', include(router.urls)),  # Includes auto-generated CRUD routes for books
]

