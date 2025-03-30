from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, generics
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

#  Pagination Class
class PostPagination(PageNumberPagination):
    page_size = 10  # Limits 10 posts per page

#  Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#  Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#  User Feed View (Fixed)
class UserFeedView(generics.ListAPIView):
    """Shows posts from users the current user follows."""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination  #  Added pagination

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Get users the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')  #  Explicit ordering
