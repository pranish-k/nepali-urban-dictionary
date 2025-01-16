from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['title', 'meaning', 'sentence']
        labels = {
            'title': 'Word',
            'meaning': 'Meaning',
            'sentence': 'Sentence',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title-field', 'id': 'word-title'}),
            'meaning': forms.Textarea(attrs={'class': 'meaning-field', 'id': 'word-meaning', 'rows': 2}),
            'sentence': forms.Textarea(attrs={'class': 'sentence-field', 'id': 'word-sentence', 'rows': 3}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=200)