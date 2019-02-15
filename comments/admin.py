from django.contrib import admin
from .models import Comment, Post

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'post']