from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pgcorp_user
from . import models

class UserSignupForm(UserCreationForm):
	username = forms.CharField(label="Username", max_length=20)
	first_name = forms.CharField(label="First Name", max_length=20)
	last_name = forms.CharField(label="Last Name", max_length=20)
	email = forms.EmailField(label="Email", max_length=50)
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=15)
	password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(), max_length=15)
	user_type = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), label="Select User type", choices=models.USER_TYPE_CHOICES)

	class Meta:
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'user_type']
		model = Pgcorp_user