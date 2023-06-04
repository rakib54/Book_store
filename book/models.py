from django.db import models

# Create your models here.


class BookstoreModel(models.Model):
    CATEGORY = (
        ('Mystrey', 'Mystrey'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
        ('humor', 'Humor'),

    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_publish = models.DateTimeField(auto_now_add=True)
    last_publish = models.DateTimeField(auto_now=True)
