from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import UserModel


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = UserModel
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = '__all__'



class UserRegisterForm(CustomUserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'phone', 'password1', 'password2', 'avatar']        
