from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pgcorp_user

class UserSignupForm(UserCreationForm):
	username = forms.CharField(label="Username", max_length=20)
	first_name = forms.CharField(label="First Name", max_length=20)
	last_name = forms.CharField(label="Last Name", max_length=20)
	email = forms.EmailField(label="Email", max_length=50)
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=15)
	password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(), max_length=15)

	class Meta:
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
		model = Pgcorp_user