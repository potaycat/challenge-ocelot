from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import Http404
from . import serializers
from .models import Book
from bson.objectid import ObjectId


class BookListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Book.objects.all()

        author = self.request.query_params.get("author")
        if author is not None:
            queryset = queryset.filter(author__contains=author)

        publish_date = self.request.query_params.get("publish_date")
        if publish_date is not None:
            queryset = queryset.filter(publish_date=publish_date)
        return queryset


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_object(self):
        qs = Book.objects.filter(_id=ObjectId(self.kwargs["pk"]))
        if qs:
            return qs[0]
        else:
            raise Http404
