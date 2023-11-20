from rest_framework.decorators import (
    api_view,
    throttle_classes,
    parser_classes,
    permission_classes,
)
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.response import Response
from rest_framework import permissions
from pymongo import MongoClient
import os
from bson.objectid import ObjectId


db = MongoClient(os.getenv("MONGO_URI"), maxPoolSize=100)[os.getenv("MONGO_DB_NAME")]
print(db.command("dbstats"))


@api_view(("POST",))
@throttle_classes(())
@permission_classes((permissions.IsAdminUser,))
def speedy_book_create(request):
    """A trade-off between speed and security."""
    d = request.data
    result = db["books_book"].insert_one(
        {
            "title": d["title"],
            "author": d["author"],
            "publish_date": d["publish_date"],
            "isbn": d["isbn"],
            "price": d["price"],
        }
    )
    return Response({"inserted_id": str(result.inserted_id)}, status=201)


@cache_page(600)
@vary_on_headers()
@api_view(("GET",))
@throttle_classes(())
@permission_classes((permissions.AllowAny,))
def speedy_book_detail(request, pk):
    collection = db["books_book"]
    obj = collection.find({"_id": ObjectId(pk)})
    try:
        obj = obj[0]
    except Exception as e:
        print(e)
        return Response({"message": "Not found."}, status=404)
    obj["_id"] = str(obj["_id"])
    return Response({"data": obj}, status=200)
