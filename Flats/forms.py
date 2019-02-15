from django import forms
from .models import FlatDetails


class FlatPostForm(forms.ModelForm):
    rent = forms.IntegerField(widget=forms.NumberInput(attrs={"value": 200}))
    
    class Meta:
        fields = ['title', 'address', 'description', 'total_rent', 'total_space', 'total_rent', 'deposit', 'possession', 'total_rooms', 'property_type', 'floor', 'parking', 'number_of_guests']
        model = FlatDetails
