from django import forms
from .models import *
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'genre ', 'summary', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }