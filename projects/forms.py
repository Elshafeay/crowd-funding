from django import forms
from .models import Donation


class DonateForm(forms.Form):
    donation = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '$1000 '}))
    user_id = forms.CharField(widget=forms.HiddenInput(attrs={'value': '1'}))

    class Meta:
        model = Donation
        # fields = ('donation', 'user_id')
