from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse

# Create your views here.
def index(request):
	t = loader.get_template('demo_webapp/index.html') # Load HTML file
	return HttpResponse(t.render())

def success(request):
	t = loader.get_template('demo_webapp/success.html') # Load HTML file
	return HttpResponse(t.render())
