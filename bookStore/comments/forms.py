from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        exclude = ['title']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        exclude = ['post']
