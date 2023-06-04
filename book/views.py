from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookstoreModel

# Create your views here.


def home(request):
    return render(request, 'base.html')


def store_book(request):
    if (request.method == 'POST'):
        book = BookStoreForm(request.POST)
        if book.is_valid():
            book.save()  # commit= False -> it won't save
            print(book.cleaned_data)
            return redirect('show_books')

    else:
        book = BookStoreForm()
    return render(request, 'store_book.html', {'form': book})


def show_books(request):
    books = BookstoreModel.objects.all()  # take all data from database
    print('ALL books', books)
    return render(request, 'show_book.html', {'books': books})
