from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import FlatDetails, Flat

# Create your views here.
class FlatPostView(CreateView):
	model = FlatDetails
	fields = ['location', 'rent']
	template_name = 'Flats/flats_post.html'
	

