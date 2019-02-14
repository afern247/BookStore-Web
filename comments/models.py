from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from bookDetails.models import Book


# Create your models here.
class Comment(models.Model):
    author        = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text          = models.CharField(max_length=150)
    #book        = models.ForeignKey(Book,on_delete=models.CASCADE)
    #Need book model to be finished to use as foreign key
    def save(self):
        self.save()
    def __str__(self):
        return self.text





