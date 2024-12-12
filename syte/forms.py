from django import forms
from .models import Text

class TextForm(forms.ModelForm):
    class Meta:
        model=Text

        fields=['text', 'text1']


class MessageForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    subject=forms.CharField(max_length=200, required=False)
    message=forms.CharField(widget=forms.Textarea)

