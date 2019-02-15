from django import forms
from .models import FlatDetails

PROPERTY_CHOICES = (
    (("apartment_flat"), ("Apartment/Flat")), 
)
class FlatPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Enter a suitable title for your flat."}
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Select a address from the address picker.", 
            "id": "address-picker-text-field"
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Enter a description for your flat.", 
            "rows": "4"}
        ))
    total_space = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter total space in square feet",
    })) 

    total_rent = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            "placeholder": "Enter amount to set as rent."
            }
        ))
    deposit = forms.CharField(widget=forms.NumberInput(
        attrs={
            "placeholder": "Enter a amount for deposit." 
        }
    ))
    total_rooms = forms.CharField(widget=forms.NumberInput(
        attrs={
            "placeholder": "Enter number of rooms available for rent",
        }
    ))
    property_type = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ), 
        choices=PROPERTY_CHOICES
    )

    class Meta:
        fields = ['title', 'address', 'description', 'total_space', 'total_rent', 'deposit', 'possession', 'total_rooms', 'property_type', 'floor', 'parking', 'number_of_guests']
        model = FlatDetails
