from django import forms
from django.core.exceptions import ValidationError
from .utils import validate_password

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not validate_password(password):
            raise ValidationError("Password does not meet the security requirements.")
        return password
