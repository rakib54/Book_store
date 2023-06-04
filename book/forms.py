from django import forms
from book.models import BookstoreModel


class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookstoreModel
        fields = ['id', 'book_name', 'author', 'category']
