from django import forms
from .models import Donation,Project


class DonateForm(forms.Form):
    donation = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '$1000 '}))
    user_id = forms.CharField(widget=forms.HiddenInput(attrs={'value': '1'}))

    class Meta:
        model = Donation
        # fields = ('donation', 'user_id')
class CreateForm(forms.Form):
    title = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title '})   )
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Details '}))
    start_date = forms.DateField( widget=forms.SelectDateWidget)
    end_date = forms.DateField( widget=forms.SelectDateWidget)
    target = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Target '}))

    # class Meta:
    #     model = Donation
