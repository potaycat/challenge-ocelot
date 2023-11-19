from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    def get_cover(self, obj):
        if obj.cover.startswith("https://challenge-ocelot.s3"):
            return obj.text
        else:
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
