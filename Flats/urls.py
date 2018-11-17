from django.conf.urls import url
from .import views

urlpatterns = [
	url(r'post/$', views.FlatPostView.as_view(), name='post'),
	url(r'(?P<hash>[\w-]{6})/(?P<slug>[\w-]+)/$', views.FlatDetailsView.as_view(), name='flat_detail'),
	url(r'all/$', views.FlatsListView.as_view(), name='all_flats'),
	url(r'(?P<hash>[\w-]{6})/(?P<slug>[\w-]+)/contac_owner/$', views.ContactOwnerView.as_view(), name='contact_owner'),
]