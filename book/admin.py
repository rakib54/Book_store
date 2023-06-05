from django.contrib import admin
from book.models import BookstoreModel
# Register your models here.


class BookstoreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'author',
                    'category', 'first_publish', 'last_publish')


admin.site.register(BookstoreModel, BookstoreModelAdmin)
