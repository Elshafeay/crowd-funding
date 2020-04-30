from django import forms
from .models import Donation,Project,Category,ProjectImages


class DonateForm(forms.Form):
    donation = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '$1000 '}))

    class Meta:
        model = Donation


class CreateForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Title '}
    ))
    details = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Details ', 'rows': '4'}
    ))
    cover = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.SelectDateWidget(
        attrs={'class': 'form-control'})
    )
    end_date = forms.DateField(widget=forms.SelectDateWidget(
        attrs={'class': 'form-control'})
    )
    images = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'multiple': True, 'class': 'form-control'}
    ))
    target = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Target '}))

    tags = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Tags Seperated by ,'
        }
    ))
