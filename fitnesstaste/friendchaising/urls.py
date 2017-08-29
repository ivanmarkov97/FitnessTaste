from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.friendchaising_main, name='friendchaising_main'),
	url(r'^about_friendchaising', views.about_friendchaising, name='about_friendchaising'),
]