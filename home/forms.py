from django import forms
from .models import *
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'author', 'genre', 'summary', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Diary'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Diary'}),
        }
