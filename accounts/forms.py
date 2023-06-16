from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'profile_picture', 'username','profile_type', 'email', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode')
        widgets = {
            'address_line1': forms.TextInput(attrs={'placeholder': 'line'}),
            'city': forms.TextInput(attrs={'placeholder': 'city'}),
            'state': forms.TextInput(attrs={'placeholder': 'state'}),
            'pincode': forms.TextInput(attrs={'placeholder': 'pincode'}),
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        return password2
