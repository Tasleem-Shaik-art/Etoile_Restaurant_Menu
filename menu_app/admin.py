from django.contrib import admin
from .models import MenuItem  # This imports your database structure

# This line tells Django to show 'Menu Items' in the Admin Dashboard
admin.site.register(MenuItem)