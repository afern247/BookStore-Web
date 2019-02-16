from django import forms
from .models import List

class CreateList(forms.ModelForm):
    list_name = forms.CharField()

    class Meta:
        model = List
        fields = ('name',)
