from django import forms
from .models import Donation


class DonateForm(forms.Form):
    donation = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '$1000 '}))
    user_id = forms.CharField(widget=forms.HiddenInput)

    # class Meta:
    #     model = Donation
