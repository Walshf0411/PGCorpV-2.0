from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic import DetailView, ListView, View
from .models import FlatDetails, FavouriteFlats, FlatApplication
from django.urls import reverse_lazy
from . import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import JsonResponse
from Accounts.forms import UserLoginForm, UserSignupForm


# Create your views here.
class FlatPostView(CreateView):
	model = FlatDetails
	template_name = 'Flats/flats_post.html'
	success_url = reverse_lazy("land_page")
	form_class = forms.FlatPostForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		self.request.session['flat_posted'] = True
		return super().form_valid(form)


class FlatDetailsView(DetailView):
	model = FlatDetails
	template_name = 'Flats/flat_details.html'
	slug_field = "slug"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data()
		if not self.request.user.is_authenticated:
			context.update({
				"login_form": UserLoginForm(), 
				"signup_form": UserSignupForm(), 
			})
		return context

	def get_object(self):
		flat = FlatDetails.objects.get(hash=self.kwargs["hash"])
		if self.request.user.is_authenticated:
			try:
				FavouriteFlats.objects.get(user=self.request.user, flat=flat)
				flat.liked = True
			except ObjectDoesNotExist:
				flat.liked = False

		return flat


class FlatsListView(ListView):
	'''List of all the flats'''
	paginate_by = 2
	model = FlatDetails
	template_name = "Flats/flats_list.html"
	context_object_name = "flats"
	queryset = FlatDetails.objects.order_by("-date_of_posting")


class ContactOwnerView(View):
	
	def get(self, request, *args, **kwargs):
		if hash in kwargs:
			hash = kwargs['hash']


class LikeFlat(View):

	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			if 'flat' in self.request.GET and 'user' in self.request.GET:
				try:
					flat = FlatDetails.objects.get(hash=self.request.GET['flat'])
					
					try:
						relation = FavouriteFlats.objects.get(user=self.request.user, flat=flat)
						relation.delete()
						count = FavouriteFlats.objects.filter(flat=flat).count()
						return JsonResponse({
							'liked': False,
							'count': count
						})
					except ObjectDoesNotExist:
						# Not already liked
						FavouriteFlats.objects.create(user=self.request.user, flat=flat)
						count = FavouriteFlats.objects.filter(flat=flat).count()
						return JsonResponse({
							'liked': True,
							'count': count
						})

				except ObjectDoesNotExist:
					count = FavouriteFlats.objects.filter(flat=flat).count()
					return JsonResponse({
							'liked': False,
							'count': count,
						})
			else:
				return JsonResponse({
					'liked': False,
					'count': 0,
				})


class FlatApplyView(View):
	
	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			if 'flat' in self.request.GET:
				try:
					flat = FlatDetails.objects.get(hash=self.request.GET['flat'])
					application, created = FlatApplication.objects.get_or_create(user=self.request.user, flat=flat)
					
					if(created):
						return JsonResponse({
							'applied': True, 
						})
					else:
						return JsonResponse({
							'previouslyApplied': True, 
						}) 
				except ObjectDoesNotExist:
					return JsonResponse({
						'applied': False, 
					})