from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={ 'placeholder': 'Maximum amount of characters: 150',
                                                            'cols': 65, 'rows': 5}))
    class Meta:
        model = Review
        fields = ['message']
        exclude = ['rating']
