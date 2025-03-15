# books/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('insert_book/', views.insert_book, name='insert_book'),
    path('read_books/', views.read_books, name = 'read_books'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('update_book/<int:book_id>/', views.update_book, name='update_book'),
    path('read_books/<int:book_id>/', views.read_books, name='read_books'),
]