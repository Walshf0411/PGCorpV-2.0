from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'$', views.LandingPage.as_view(), name="land_page"),
]