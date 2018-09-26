from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import FlatDetails, Flat
from django.urls import reverse_lazy

# Create your views here.
class FlatPostView(CreateView):
	model = FlatDetails
	fields = ['location', 'rent']
	template_name = 'Flats/flats_post.html'
	success_url = reverse_lazy("land_page")

	def form_valid(self, form):
		flat = Flat()
		flat.user = self.request.user
		flat.save()
		form.instance.flat = flat
		return super().form_valid(form)
