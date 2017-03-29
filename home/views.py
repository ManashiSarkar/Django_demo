from django.shortcuts import render

# Create your views here.

def invalidurl(request):
	return render(request, 'home/invalidurl.html', {})

def index(request):
	return render(request, 'home/index.html', {})
