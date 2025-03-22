from django.contrib import admin
from .models import Post  # Ensure this import appears only once


# Register your models here.
admin.site.register(Post)  # Ensure this is not duplicated