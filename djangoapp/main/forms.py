from django import forms


class SearchForm(forms.Form):
    current_search = forms.CharField(label="Enter Title", max_length=100)