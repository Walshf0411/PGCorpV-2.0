from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^signup/$', views.UserSignupView.as_view(), name='signup'),
	url(r'^login/$', views.UserLoginView.as_view(), name='login'),
	url(r'^logout/$', views.UserLogoutView.as_view(), name='logout'),
	url(r'profile/$', views.UserProfileView.as_view(), name='profile'),
	url(r'password_change/$', views.UserPasswordChangeView.as_view(), name='password_change'), 
	url(r'password_change/done/$', views.UserPasswordChangeDoneView.as_view(), name='password_change_done'),
	url(r'update/', views.UpdateProfileView.as_view(), name='update'),
]
