from django.urls import path
from . import views # This imports the code from your views.py

urlpatterns = [
    # This makes the menu the home page (http://127.0.0.1:8000/)
    path('', views.menu_view, name='menu'),
    path('order/', views.place_order, name='place_order'),
]