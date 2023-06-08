from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        label='Search Query',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your search query'})
    )
