from django.urls import path
from . import views

urlpatterns = (
    path("", views.BookListCreateAPIView.as_view(), name="list-books"),
    path("<id>", views.BookDetailAPIView.as_view(), name="book-detail"),
)
