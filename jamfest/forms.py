from django import forms
from .models import NewsLetterRecipients

<<<<<<< HEAD
class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetterRecipients
        fields = ['name','email']
        
=======
class NewsLetterForm(forms.Form):
    # your_name = forms.CharField(label='First Name', max_length=30) testing out
    email = forms.EmailField(label='Email')
>>>>>>> c008b7a8ee0a6da848a108f453da3f912713b898
