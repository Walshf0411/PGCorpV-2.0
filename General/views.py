from django.shortcuts import render
from django.contrib.auth.views import TemplateView
from django.views import View
from django.http import JsonResponse
from Flats.models import FlatDetails
from django.views.generic import ListView
from Flats.views import FlatsListView
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

		if self.request.session.get('user_created', None):
			message = "Thanking you for signing up for PGCorp.You can login to continue."
			context.update({
				'show_notif': True,
				'notif_message': message,
				'color': 'blue',
				})

		if self.request.session.get('flat_posted', None):
			message = "Your flat has been posted successfully. You can view it on the page."
			context.update({
				'show_notif': True,
				'notif_message': message,
				'color': 'green',
				})

		if 'user_logged_in' in self.request.session:	
			del(self.request.session['user_logged_in'])		

		if 'user_created' in self.request.session:	
			del(self.request.session['user_created'])

		if 'flat_posted' in self.request.session:
			del(self.request.session['flat_posted'])

		return context
	
class AjaxBasedSearch(View):
	
	def get(self, request, *args, **kwargs):
		string = request.GET['data']
		results = list(map(lambda x:x.title, FlatDetails.objects.filter(location__contains=string)))
		json = {
			'results': results,
		}
		return JsonResponse(json)

class Search(FlatsListView):
	template_name = 'General/search_results.html'

	def get_context_data(self):
		context = super().get_context_data()
		context.update({'query': self.request.GET['search']})
		return context

	def get_queryset(self):
		search = self.request.GET['search']
		return FlatDetails.objects.filter(location__contains=search)
