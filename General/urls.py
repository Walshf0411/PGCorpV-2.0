from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from PGCorpV2 import settings

urlpatterns = [
	url(r'search_suggestions/$', views.AjaxBasedSearch.as_view(), name='ajax-search'),
	url(r'search/$', views.Search.as_view(), name='search'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)