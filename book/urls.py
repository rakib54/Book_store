from django.urls import path
# from book.views import home, store_book, show_books, edit_book, delete_books
from . import views

urlpatterns = [
    # path('', views.home),
    path('', views.MyTemplateView.as_view()),
    path('store_new_book/', views.store_book, name="store_book"),
    # path('show_books/', views.show_books, name="show_books"),
    path('show_books/', views.BookListView.as_view(), name="show_books"),
    path('book_details/<int:id>',
         views.BookDetailView.as_view(), name="book_details"),
    path('edit_books/<int:id>', views.edit_book, name="edit_books"),
    path('delete_books/<int:id>', views.delete_books, name="delete_books"),
]
