from django.shortcuts import render, redirect
from django.contrib.auth.views import (
	LoginView, 
	LogoutView,
	PasswordChangeView, 
	PasswordChangeDoneView)
from .forms import UserSignupForm, UserLoginForm
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from Flats.models import FlatDetails, FlatApplication
from Accounts import models
from django.core.paginator import Paginator
from django.views.generic import View
from django.http import JsonResponse
from .models import Pgcorp_user
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags
from Accounts.models import User_Type
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
		subject = 'Registration Succesful.'
		username = form.cleaned_data['username']
		user_type = User_Type()
		html_message = render_to_string(
			'General/mail_templates/registrationSuccess.html', 
			context={
				'username': username,
				'email': form.cleaned_data['email'], 
				'user_type': user_type.user_type_string(form.cleaned_data['user_type']), 
				'first_name': form.cleaned_data['first_name'], 
				'last_name': form.cleaned_data['last_name'], 
			}
		)
		plain_message = strip_tags(html_message)
		
		send_mail(
			subject, 
			plain_message, 
			"pgcorpservice@gmail.com", 
			[form.cleaned_data['email'], ], 
			html_message=html_message, 
			fail_silently=False
		) 
		return super().form_valid(form)


class UserLoginView(LoginView):
	template_name = 'Accounts/login.html'
	form_class = UserLoginForm

	def form_valid(self, form):
		
		return super().form_valid(form)


class UserLogoutView(LogoutView):
	
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)


class UserProfileView(TemplateView):
	template_name = 'Accounts/dashboard_base.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		if self.request.user.is_authenticated:
			if self.request.user.pgcorp_user.user_type == User_Type.HOUSE_OWNER:
				flats_posted = FlatDetails.objects.filter(user=self.request.user).order_by("-date_of_posting")
				paginator = Paginator(flats_posted, 2)
				flats_posted = paginator.page(1)

				if 'page' in self.request.GET: 
					flats_posted = paginator.page(self.request.GET['page'])

				context.update({
					"user_type": "House Owner",
					"flats": flats_posted,
				})
			elif self.request.user.pgcorp_user.user_type == User_Type.PAYING_GUEST:
				flats_applied = FlatApplication.objects.filter(user=self.request.user)
				paginator = Paginator(flats_applied, 7)
				flats_applied =  paginator.page(1)

				if 'page' in self.request.GET:
					flats_applied = paginator.page(self.request.GET['page'])

				context.update({
					"user_type": "Paying Guest", 
					"flats": flats_applied, 
				})
		
		return context


class UserPasswordChangeView(PasswordChangeView):
	template_name = 'Accounts/password_change.html'
	success_url = reverse_lazy('password_change_done')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
	template_name = 'Accounts/password_change_done.html'


class UpdateProfileView(TemplateView):
	template_name = 'Accounts/update_profile.html'


class UpdateProfilePicture(View):
	
	def post(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			if 'profile_picture' in self.request.POST:
				self.request.user.pgcorp_user.profile_picture = self.request.POST['profile_picture']
				return JsonResponse({
					"success": "profile picture updated"
				})
