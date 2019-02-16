from django.db import models
from users.models import Profile

# Create your models here.
class Post(models.Model):
    title         = models.CharField(max_length=50)

class Comment(models.Model):
    author        = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    text          = models.CharField(max_length=150)
    post          = models.ForeignKey(Post, on_delete=models.CASCADE, default="")
    #book        = models.ForeignKey(Book,on_delete=models.CASCADE)
    #Need book model to be finished to use as foreign key
    def save(self):
        self.save()
    def __str__(self):
        return self.text