from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from .models import FlatDetails, Flat
from django.urls import reverse_lazy

# Create your views here.
class FlatPostView(CreateView):
	model = FlatDetails
	fields = ['title', 'location', 'rent']
	template_name = 'Flats/flats_post.html'
	success_url = reverse_lazy("land_page")

	def form_valid(self, form):
		flat = Flat()
		flat.user = self.request.user
		flat.save()
		form.instance.flat = flat
		self.request.session['flat_posted'] = True
		return super().form_valid(form)

class FlatDetailsView(DetailView):
	model = FlatDetails
	template_name = 'Flats/flat_details.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data()
		user = context['flatdetails'].flat.user
		context.update({"user": user})
		return context

	def get_object(self):
		flat = FlatDetails.objects.get(hash=self.kwargs["hash"])
		return flat

class FlatsListView(ListView):
	'''List of all the flats'''
	model = FlatDetails
	template_name = "Flats/flats_list.html"
	context_object_name = "flats"