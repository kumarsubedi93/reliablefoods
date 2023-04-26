
from django import forms
class FeedbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}), required=True, max_length=100)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email'}), required=True, max_length=100)
    description  = forms.CharField(widget=forms.Textarea)