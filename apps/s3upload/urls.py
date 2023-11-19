from django.urls import path
from . import views

urlpatterns = (
    path('upload-url', views.CreatePresignedS3UrlAPIView.as_view(), name="s3-presigned"),
)