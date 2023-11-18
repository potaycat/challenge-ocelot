from django.urls import path
from . import views

urlpatterns = (
    path("books/", views.speedy_book_create),
    path("books/<pk>", views.speedy_book_detail),
)
