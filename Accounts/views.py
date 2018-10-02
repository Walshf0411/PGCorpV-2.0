from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
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

	def form_valid(self, form):
		self.request.session['user_created'] = True
		return super().form_valid(form)

class UserLoginView(LoginView):
	template_name = 'Accounts/login.html'

	def form_valid(self, form):
		self.request.session['user_logged_in'] = True
		return super().form_valid(form)

class UserLogoutView(LogoutView):
	
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)