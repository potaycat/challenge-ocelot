from django.shortcuts import render
from rest_framework import (
    mixins,
    generics,
    status,
    filters,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import serializers
from .models import Book


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
