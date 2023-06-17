from django import forms


class SearchForm(forms.Form):
    searched_titles = forms.CharField(label="Enter Title", max_length=100)
