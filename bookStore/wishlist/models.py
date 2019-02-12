from django.db import models
from datetime import datetime

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=25)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=50)
    price = models.IntegerField()
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    list_name = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.name