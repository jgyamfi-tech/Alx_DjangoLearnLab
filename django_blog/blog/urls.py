from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,CommentCreateView, CommentUpdateView, CommentDeleteView
)


urlpatterns = [
    # Authentication & Profile Views
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),

    # Blog Post CRUD Views
    path("posts/", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("posts/<int:post_id>/comments/new/", views.add_comment, name="add_comment"),
    path("comments/<int:comment_id>/edit/", views.edit_comment, name="edit_comment"),
    path("comments/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),
    path("posts/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-update"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]


