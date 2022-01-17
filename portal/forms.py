from django.contrib.auth.models import User
from .models import Article
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


# class NewsForm(forms.ModelForm):
#
#     class Meta:
#         model = Article
#         fields = ['article_type', 'title', 'author', 'description', 'url']

