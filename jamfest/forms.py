from django import forms
from .models import NewsLetterRecipients

class NewsLetterForm(forms.Form):
    # your_name = forms.CharField(label='First Name', max_length=30) testing out
    email = forms.EmailField(label='Email')
