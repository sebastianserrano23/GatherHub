from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=35, required=True, help_text='user name must be 35 characters or fewer')

    class Meta:
        model = User
        fields = ('username', 'email', 'pasword')
