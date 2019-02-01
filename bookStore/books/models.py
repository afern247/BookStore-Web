from django.db import models

class Comment(models.Model):
    user        = models.CharField(max_length=100)
    text_body   = models.CharField(max_length=150)
    created     = models.DateTimeField(auto_now_add=True)
