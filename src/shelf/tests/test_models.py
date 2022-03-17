from django.db.utils import IntegrityError
from django.test import TestCase

from shelf.models import Book


book_params = {
        'name': 'A Space Odyssey',
        'genre': 'science fiction',
        'page_number': 675,
        'publisher': 'Hutchinson',
        'author': 'Arthur Charles "C." Clarke'
}


class BookModelTests(TestCase):

    def test_success_book_create(self):
        book = Book.objects.create(**book_params)
        self.assertEqual(book_params['name'], book.name, msg='Book name is not equal')
        self.assertEqual(book_params['publisher'], book.publisher, msg='Publisher name is not equal')

    def test_book_unique_name(self):
        Book.objects.create(**book_params)
        try:
            Book.objects.create(**book_params)
            raise ValueError('UNIQUE name check failed')
        except IntegrityError:
            pass

    def test_book_create_incomplete_data(self):
        try:
            Book.objects.create(**book_params.pop('author'))
            raise ValueError('Incomplete create-data check failed')
        except TypeError:
            pass
