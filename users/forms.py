from django import forms
from users.models import UserProfile
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    pass_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    fav_song = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    fav_artist = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    profile_pic = forms.ImageField(required=False)

class EditForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    fav_song = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    fav_artist = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    profile_pic = forms.ImageField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':"username", 'placeholder':"Type your username", 'required':True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':"pass", 'placeholder':"Type your username", 'required':True}))