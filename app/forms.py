from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Customers


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'auto-focous':'True', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'auto-complete':'current-password','class':'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocous':'True', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='old-password',widget=forms.PasswordInput(attrs={'autofocous':'True','autocomplete':'current-password','class':'form-control'})),
    new_password1 = forms.CharField(label='new-password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})),
    new_password2 = forms.CharField(label='coniform-password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})),
class MyPasswordResetForm(PasswordChangeForm):
    pass


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['id','name','locality','city','mobile','state','zipcode']
        widget={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),

        }
