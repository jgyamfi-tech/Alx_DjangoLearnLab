from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import PostViewSet, CommentViewSet, UserFeedView

# API Schema (Swagger) Configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Social Media API",
        default_version='v1',
        description="API documentation for posts and comments",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],  # Adjust as needed
)

# Initialize router
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

#  Define URL patterns (Removed Duplicate Code)
urlpatterns = [
    path('', include(router.urls)),  
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
]
