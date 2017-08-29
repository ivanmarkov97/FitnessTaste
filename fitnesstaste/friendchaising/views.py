from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def friendchaising_main(request):
	contex = {

	}
	return render(request, 'friendchaising/friendchaising.html', contex)

def about_friendchaising(request):
	return HttpResponse('about_friendchaising')