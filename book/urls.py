from django.urls import path
from book.views import home, store_book, show_books, edit_book, delete_books

urlpatterns = [
    path('', home),
    path('store_new_book/', store_book, name="store_book"),
    path('show_books/', show_books, name="show_books"),
    path('edit_books/<int:id>', edit_book, name="edit_books"),
    path('delete_books/<int:id>', delete_books, name="delete_books"),
]
