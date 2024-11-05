from django import forms
from apps.home.models import Contact

class ContactForm(forms.Form):
    name =  forms.CharField(
        max_length=25,
        error_messages={'required': 'Name is required.'},
        widget=forms.TextInput(attrs={'placeholder': ' Name'})
    )
    email =  forms.CharField(
        max_length=320,
        error_messages={'required': 'Email is required.'},
        widget=forms.TextInput(attrs={'placeholder': ' Email'})
    )
    phone =  forms.CharField(
        max_length=15,
        error_messages={'required': 'Phone is required.'},
        widget=forms.TextInput(attrs={'placeholder': ' Phone'})
    )
    subject =  forms.CharField(
        error_messages={'required': 'Subject is required.'},
        widget=forms.TextInput(attrs={'placeholder': ' Subject'})
    )
    message = forms.CharField(
        error_messages={'required': 'Message is required.'},
        widget=forms.Textarea(attrs={'placeholder': 'Message'})
    )
    is_notify = forms.BooleanField(required=False)    