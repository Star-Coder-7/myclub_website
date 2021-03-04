from django import forms
from django.forms import ModelForm
from .models import Venue


# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zipCode', 'phone', 'web', 'email')

        labels = {
            'name': '',
            'address': '',
            'zipCode': '',
            'phone': '',
            'web': '',
            'email': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Address'}),
            'zipCode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Zip code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone/Contact Number'}),
            'web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Web URL'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }
