from django.shortcuts import render
from django.contrib.auth.views import TemplateView
from django.views import View
from django.http import JsonResponse
from Flats.models import FlatDetails
from django.views.generic import ListView
# Create your views here.

class LandingPage(TemplateView):
	template_name = 'General/landing_page.html'
	
class AjaxBasedSearch(View):
	
	def get(self, request, *args, **kwargs):
		string = request.GET['data']
		results = list(map(lambda x:x.title, FlatDetails.objects.filter(title__contains=string)))
		json = {
			'results': results,
		}
		return JsonResponse(json)

class Search(ListView):
	template_name = 'General/search_results.html'
	model = FlatDetails
	queryset = None
	context_object_name = "flats"

	def dispatch(self, request, *args, **kwargs):
		search = request.GET.get("search", "")
		self.queryset = FlatDetails.objects.filter(title__contains=search)
		return super().dispatch(request, args, kwargs)