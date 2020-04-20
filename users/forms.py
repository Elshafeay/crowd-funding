from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserModel


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = UserModel
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = '__all__'
