from django.shortcuts import render
from clubs.models import Club

# Create your views here.
def clubs_main(request):
	context = {
		'all_clubs' : Club.objects.all(),
	}
	return render(request, 'clubs/clubs.html', context)