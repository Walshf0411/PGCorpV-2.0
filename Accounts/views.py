from django.shortcuts import render
from django.contrib.auth.views import (
	LoginView, 
	LogoutView,
	PasswordChangeView, 
	PasswordChangeDoneView)
from .forms import UserSignupForm
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from Flats.models import FlatDetails, Flat

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

class UserProfileView(TemplateView):
	template_name = 'Accounts/user_profile.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		# current user
		user = self.request.user
		flats_posted = Flat.objects.filter(user=user)
		flats_posted = map(lambda x: x.flatdetails_set.all(), flats_posted)
		flats_posted = map(lambda x: x[0], flats_posted) 
		context.update({
			'flats_posted': list(flats_posted),
		})
		return context


class UserPasswordChangeView(PasswordChangeView):
	template_name = 'Accounts/password_change.html'
	success_url = reverse_lazy('password_change_done')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
	template_name = 'Accounts/password_change_done.html'