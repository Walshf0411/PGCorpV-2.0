from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'search_suggestions/$', views.AjaxBasedSearch.as_view(), name='ajax-search'),
	#url(r'search/$', views.Search.as_view(), name='search'),
]