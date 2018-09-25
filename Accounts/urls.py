from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^signup/$', views.UserSignupView.as_view(), name='signup'),
	url(r'^login/$', views.UserLoginView.as_view(), name='login'),
]
