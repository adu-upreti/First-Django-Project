from django import forms
from .models import Tweet


class TweetForm(forms.ModelFormodel):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']