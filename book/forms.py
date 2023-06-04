from django import forms
from book.models import BookstoreModel


class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookstoreModel
        exclude = ['last_publish', 'first_publish']
