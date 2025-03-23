from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from taggit.forms import TagWidget


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
        


class CommentForm(forms.ModelForm):
   class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
       

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long.")
        return content


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # Provides an input for tags
        }
