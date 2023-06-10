
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    contact_details = forms.CharField(max_length=100)
    organization = forms.CharField(max_length=100)
    email_id= forms.EmailField()
    registration_date = forms.DateField()
    registration_time = forms.TimeField()
    # password=forms.CharField(max_length=256)
    class Meta:
        model = User
        fields = ['name', 'contact_details', 'organization', 'registration_date', 'registration_time']
