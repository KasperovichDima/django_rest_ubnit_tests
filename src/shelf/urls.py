from django.urls import path

from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


app_name = 'book'

urlpatterns = [
    path('book_create/', generics.CreateAPIView.as_view(
        serializer_class=BookSerializer),
        name='create'
         ),
    path('book_list/', generics.ListAPIView.as_view(
        queryset=Book.objects.all(),
        serializer_class=BookSerializer),
        name='list'
         ),
    path('book_edit/<int:pk>/', generics.RetrieveUpdateDestroyAPIView.as_view(
        serializer_class=BookSerializer,
        queryset=Book.objects.all()),
        name='edit'
         ),
]
