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
    phone = forms.RegexField(regex="^(002)?01[0125]\d{8}$")

    def __init__(self, data=None, files=None, *args, **kwargs):
        super().__init__(data=data, files=files, *args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['avatar'].widget.attrs['class'] = 'form-control custom-file-input'

    class Meta:
        model = UserModel
        fields = [
            'first_name', 'last_name', 'email',
            'phone', 'password1', 'password2', 'avatar'
        ]

class UserUpdateForm(CustomUserChangeForm):
    email = None
    phone = forms.RegexField(regex = "^(002)?01[0125]\d{8}$")
    password1 = None
    password2 = None
    def __init__(self, data=None, files=None, *args, **kwargs):
        super().__init__(data=data, files=files, *args, **kwargs)
        self.fields['country'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = UserModel
        fields = [
            'first_name', 'last_name', 
            'country', 'birth_date', 
            'facebook_profile', 'phone', 
            'avatar'
        ]        
