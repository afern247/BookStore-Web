from django.shortcuts import render
from django import forms
from .models import Comment

# Create your forms here.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

