from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import UserSignupForm
from django.views.generic.edit import CreateView

# Create your views here.
# A view is a basically the main processing unit of an app
# every view is mapped to a url 
# whenever a url is requested the related view will be executed

# we have extended this default authentication class to add customization
# also we extend django's  to get our data automatically saved to the db
class UserSignupView(CreateView):
	template_name = 'Accounts/signup.html'
	form_class = UserSignupForm
	success_url = '/'

class UserLoginView(LoginView):
	template_name = 'Accounts/login.html'
	success_url = '/'