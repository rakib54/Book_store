from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookstoreModel
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.


# def home(request):
#     return render(request, 'home.html')

# class based view

class MyTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name': 'Rakib'}
        return context


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


# def show_books(request):
#     books = BookstoreModel.objects.all()  # take all data from database
#     print('ALL books', books)
#     return render(request, 'show_book.html', {'books': books})

# class Base view for show books
class BookListView(ListView):
    model = BookstoreModel
    template_name = 'show_book.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = BookstoreModel
    template_name = 'book_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'


def edit_book(request, id):
    book = BookstoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if (request.method == 'POST'):
        form = BookStoreForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    return render(request, 'store_book.html', {'form': form})


def delete_books(request, id):
    book = BookstoreModel.objects.get(pk=id).delete()
    return redirect('show_books')
