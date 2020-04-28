from django import forms
from .models import Donation,Project,Category,ProjectImages


class DonateForm(forms.Form):
    donation = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '$1000 '}))

    class Meta:
        model = Donation




class CreateForm(forms.Form):
    title = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title '})   )
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Details ','rows':'4'}))
    cover = forms.ImageField()
    # category_id = forms.CharField(widget=forms.Select(choices=categories))
    start_date = forms.DateField( widget=forms.SelectDateWidget)
    end_date = forms.DateField( widget=forms.SelectDateWidget)
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    target = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Target '}))

