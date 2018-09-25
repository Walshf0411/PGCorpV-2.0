from django.shortcuts import render
from django.contrib.auth.views import TemplateView
# Create your views here.

class LandingPage(TemplateView):
	template_name = 'General/landing_page.html'
	
