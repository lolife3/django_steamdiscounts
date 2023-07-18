from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SearchForm(forms.Form):
    searched_titles = forms.CharField(label="Enter Title", max_length=100)


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")
