from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.clubs_main, name='clubs_main'),
]