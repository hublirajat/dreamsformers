from django import forms
from django.forms.widgets import Input

class BookingCreationForm(forms.Form):

        origin = forms.CharField(max_length=10, required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
        destination = forms.CharField(max_length=10, required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	traveldate = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker form-control'}))
