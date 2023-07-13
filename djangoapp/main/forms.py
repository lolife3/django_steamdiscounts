from django import forms
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    searched_titles = forms.CharField(label="Enter Title", max_length=100)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")
