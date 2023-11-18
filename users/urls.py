from django.urls import path
from . import views

urlpatterns = (
    path("staff", views.CreateUserView.as_view(), name="add-staff"),
)
