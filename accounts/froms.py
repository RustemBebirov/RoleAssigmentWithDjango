from django.db.models import fields
from accounts.models import Customer
from django import forms
from django.contrib.auth import get_user_model
from django.db import models
from django.forms.models import ModelForm
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    
    
	class Meta:
		model = User
		fields = ('username', 'email','create','read','update','read','delete' ,'password1', 'password2')

      

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class Login(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username'
    }))

    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Password'
    }))


class ChangeEmail(forms.Form):
    email = forms.CharField(max_length=50,widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Email'
    }))
