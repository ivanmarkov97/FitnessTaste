from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
	contex = {

	}
	return render(request, 'fitnesstaste/main_page.html', contex)

def form(request):
	contex = {

	}
	return render(request, 'fitnesstaste/form.html', contex)