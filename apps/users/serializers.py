from rest_framework import serializers
from django.contrib.auth import get_user_model
import re

UserModel = get_user_model()
email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    def validate_email(self, attr):
        if re.fullmatch(email_regex, attr):
            return attr
        else:
            raise Exception("Invalid email format.")

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            is_staff=True,
            is_superuser=True,
        )

        return user

    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "email",
            "password",
        )
