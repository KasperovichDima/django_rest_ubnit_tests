from django.db import models


class Book(models.Model):

    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Book name')
    genre = models.CharField(max_length=100)
    page_number = models.PositiveSmallIntegerField(verbose_name='Number of pages')
    publisher = models.CharField(max_length=100, db_index=True, verbose_name='Book publisher')
    author = models.CharField(max_length=100, db_index=True, verbose_name='Book author')
