from django import forms
from .models import FlatDetails

class FlatPostForm(forms.ModelForm):
    rent =  forms.IntegerField(widget=forms.NumberInput(attrs={"value": 200}))
    
    class Meta:
        fields = ['title', 'location', 'rent']
        model = FlatDetails