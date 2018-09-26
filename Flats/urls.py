from django.conf.urls import url
from .import views

urlpatterns = [
	url(r'post/$', views.FlatPostView.as_view(), name='post'),
	url(r'(?P<hash>[a-zA-Z0-9]+)/(?P<slug>[a-zA-Z0-9]+)/$', views.FlatDetailsView.as_view(), name='flat_details'),
]