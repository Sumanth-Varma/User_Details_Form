from django.forms import ModelForm
from django import forms
from .models import UserDetails
from django.core.validators import RegexValidator

alphacharvalid = RegexValidator(r'^[a-zA-Z\s]*$', 'Only alpha characters are allowed.')

class user_form_details(forms.Form):
    name = forms.CharField(label="Name",help_text='',required=True,max_length=100,validators=[alphacharvalid],widget=forms.TextInput(
        attrs={'placeholder': 'Name*','style':'width:80%;'}))
    email = forms.EmailField(label="Email*", required=True, max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Email Id*','style':'width:80%;'}))
    
    def __init__(self, *args, **kwargs):
        super(user_form_details, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['email'].label = ""