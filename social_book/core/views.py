from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# index html is main page, put bill's main page as index.html in templates
def index(request):
    return render(request, 'index.html')

def our_team(request):
    return render(request, 'out-team.html')

def profile_page(request):
    return render(request, 'profile-page.html')

def search(request):
    return render(request, 'search.html')
            