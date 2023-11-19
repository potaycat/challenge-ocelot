from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

import os
import boto3
from botocore.config import Config


s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=os.getenv("AWS_REGION"),
    config=Config(signature_version="s3v4"),
)


class CreatePresignedS3UrlAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if not (file_name := request.data.get("file")):
            return Response(status=status.HTTP_417_EXPECTATION_FAILED)

        if "image" not in (file_type := request.data.get("type", "")):
            return Response(status=status.HTTP_403_FORBIDDEN)

        presigned = s3.generate_presigned_post(
            Bucket=os.getenv("AWS_BUCKET_NAME"),
            Key="book_cover/" + file_name,
            Conditions=[],
            ExpiresIn=300,  # seconds
        )
        return Response(data=presigned, status=status.HTTP_200_OK)
