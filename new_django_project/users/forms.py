from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#class that inherits from the UserCreationForm created before
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    #only the fields the user can modify here 
    class Meta:
        model = User
        fields = ["username", "email"]
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]