from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView, View
from .models import FlatDetails, FavouriteFlats
from django.urls import reverse_lazy
from . import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import JsonResponse


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
		user = context['flatdetails'].user
		context.update({"user": user})
		return context

	def get_object(self):
		flat = FlatDetails.objects.get(hash=self.kwargs["hash"])
		if self.request.user.is_authenticated:
			try:
				FavouriteFlats.objects.get(user=self.request.user, flat=flat)
				print("liked, icon should be filled.")
				flat.liked = True
			except ObjectDoesNotExist:
				print("no liked, icon shoudl not be filled")
				flat.liked = False

		return flat


class FlatsListView(ListView):
	'''List of all the flats'''
	paginate_by = 2
	model = FlatDetails
	template_name = "Flats/flats_list.html"
	context_object_name = "flats"
	queryset = FlatDetails.objects.order_by("datetime")


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
						return JsonResponse({
							'liked': False,
						})
					except ObjectDoesNotExist:
						# Not already liked
						FavouriteFlats.objects.create(user=self.request.user, flat=flat)
						return JsonResponse({
							'liked': True,
						})

				except ObjectDoesNotExist:
					return JsonResponse({
							'liked': False,
						})
			else:
				return JsonResponse({
					'liked': False,
				})