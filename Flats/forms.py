from django import forms
from .models import FlatDetails

PROPERTY_CHOICES = (
    (("Apartment/Flat"), ("Apartment/Flat")), 
)
PARKING_OPTIONS = (
    ("No parking", "No Parking"), 
    ("2 Wheeler", "2 Wheeler"), 
    ("4 Wheeler", "4 Wheeler"), 
)

POSESSION_CHOICES = (
    ("Immediately", "Immediately"), 
    ("After 1 Month.", "After 1 Month."), 
    ("After 1 to 3 Months", "After 1 to 3 Months"), 
    ("After 3 to 9 Months", "After 3 to 9 Months"),
    ("After 6 to 9 Months", "After 6 to 9 Months"),
    ("After 9 to 12 Months", "After 9 to 12 Months"),
    ("After 1 year or above", "After 1 year or above"),
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
    parking_options = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ), 
        choices=PARKING_OPTIONS
    )
    possession = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ), 
        choices=POSESSION_CHOICES
    )
    number_of_guests = forms.IntegerField(help_text="All the guest living in the house will pay equal rent, that will be deduced by dividing the total rent by the number of guests.")
    class Meta:
        fields = ['title', 'address', 'description', 'total_space', 'total_rent', 'deposit', 'possession', 'total_rooms', 'property_type', 'floor', 'parking_options', 'number_of_guests']
        model = FlatDetails
