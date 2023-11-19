from djongo import models

# Create your models here.


class Book(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=70)
    publish_date = models.DateField()
    isbn = models.CharField(max_length=13)
    price = models.FloatField()
    cover = models.CharField(max_length=200, default=None)
