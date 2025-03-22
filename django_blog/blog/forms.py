from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# If you have a Profile model linked to the User, update this accordingly.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User  # If you have a Profile model, replace 'User' with 'Profile'
        fields = ['username', 'email']  # Modify fields as needed

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

