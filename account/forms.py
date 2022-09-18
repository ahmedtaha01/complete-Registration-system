from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate
from .models import User
# from phonenumber_field.modelfields import PhoneNumberField
# from .models import Users
# from phonenumber_field.modelfields import PhoneNumberField



class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        max_length=100, required=True, help_text='Enter Email Address', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
        ), )

    first_name = forms.CharField(
        max_length=100, required=True, help_text='Enter First Name', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First Name'}
        ), )
    last_name = forms.CharField(
        max_length=100, required=True, help_text='Enter Last Name', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last Name'}
        ), )
    username = forms.CharField(
        max_length=200, required=True, help_text='Enter Username', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        ), )
    password1 = forms.CharField(
        help_text='Enter Password', required=True, widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ), )
    password2 = forms.CharField(
        required=True, help_text='Enter Password Again', widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password Again'}
        ), )

    # phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...')
    #
    # phone = forms.CharField( validators=[phone_regex], max_length=14)
    #
    # phone = PhoneNumberField()
    check = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2' ]


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

