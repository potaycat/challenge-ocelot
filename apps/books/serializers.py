from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    def validate_cover(self, attr):
        if attr.startswith("https://challenge-ocelot.s3"):
            return attr
        raise Exception("Invalid image URL.")

    class Meta:
        model = Book
        fields = (
            "_id",
            "title",
            "author",
            "publish_date",
            "isbn",
            "price",
            "cover",
        )
