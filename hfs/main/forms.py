from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Investor


class UserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control signup-name','type':'text','required':'required', 'id':'signup-name', 'name':'signup-fullname', 'placeholder':'Full Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control signup-email','type':'email','required':'required', 'id':'signup-email', 'name':'signup-username', 'placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control signup-password','type':'password','required':'required', 'id':'signup-password', 'name':'signup-password1', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control signup-password','type':'password','required':'required', 'id':'signup-password', 'name':'signup-password2', 'placeholder':'Confirm password'}))
    class Meta:
        model = User
        fields = ('first_name','username','password1' ,'password2' )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control signin-email','type':'email','required':'required', 'id':'signin-email', 'name':'username', 'placeholder':'Email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control signin-password','type':'password','required':'required', 'id':'signin-password', 'name':'password', 'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ('username','password' )

INVESTMENT_CHOICES = [
 ("Lender","Lender"),
 ("Private Investor","Private Investor"),
 ("Employer","Employer"),
]

class InvestorForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Full Legal Names','required':'required'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email Address','required':'required'}))
    phone = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'254123456789','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==12) return false;','required':'required'}))
    investment = forms.ChoiceField(choices=INVESTMENT_CHOICES)

    class Meta:
        model = Investor
        fields = '__all__'
