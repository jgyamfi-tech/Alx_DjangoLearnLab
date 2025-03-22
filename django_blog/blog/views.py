from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile

# Create your views here.

def home(request):
    return render(request, 'blog/index.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)  # Create profile for new user
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("profile")
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, "blog/login.html")

def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    return render(request, "blog/profile.html", {"u_form": u_form, "p_form": p_form})

