from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.
def details(request):
    return render(request, 'details/Details.html')

def add_comment(request):
    post = get_object_or_404(Post)
    if request.method == "POST":
        form = CommentForm(request.Post)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('details/Details.html')
    else:
        form = CommentForm()
    return render(request, 'details/add_comment.html', {'form' : form})
