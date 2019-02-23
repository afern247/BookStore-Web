from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings

class List(models.Model):
    #user = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    user_name = models.CharField(max_length=150, default="Testing")

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    list_name = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.name