from django import forms
from .models import NewsLetterRecipients

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetterRecipients
        fields = ['name','email']
        
