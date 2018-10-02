from django.shortcuts import render
from django.contrib.auth.views import TemplateView
from django.views import View
from django.http import JsonResponse
from Flats.models import FlatDetails
from django.views.generic import ListView
# Create your views here.

class LandingPage(TemplateView):
	template_name = 'General/landing_page.html'

	def get_context_data(self):
		context = super().get_context_data()
		if self.request.session.get('user_logged_in', None):
			# the is_logged_in is true therefore, we will tell the template 
			# to show the notification and then delete the session variable
			message = "You have been logged in successfully."
			context.update({
				'show_notif': True,
				'notif_message': message,
				'color': 'green',
				})

		if 'user_logged_in' in self.request.session:	
			del(self.request.session['user_logged_in'])		

		return context
	
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