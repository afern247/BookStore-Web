from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from .forms import CommentForm


#Book model must be finished to use as foreign key and let users add comments to
#bookDetails page
'''
def add_comment(request, pk):
    addComment = get_object_or_404(book, pk=pk)
    if request.method == "POST":
        form = CommentForm(requst.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect(,pk=book.pk)
        else:
            form = CommentForm()
        return render(request, '', {'form':form})
'''