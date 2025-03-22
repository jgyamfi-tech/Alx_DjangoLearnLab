from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
     path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
]
