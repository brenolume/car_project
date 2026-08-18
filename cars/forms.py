from django import forms
from cars.models import Brand, Model

class CarForm(forms.Form):
    model = forms.CharField(max_length=100)
    brand = forms.ModelChoiceField(Brand.objects.all())
    model = forms.IntengerField()