from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse

def home(request):
	t = loader.get_template('polls/home.html')
	return HttpResponse(t.render())

def strings(request):
	t = loader.get_template('polls/strings.html')
	return HttpResponse(t.render())

def numbers(request):
	t = loader.get_template('polls/numbers.html')
	return HttpResponse(t.render())

def about(request):
	t = loader.get_template('polls/about.html')
	return HttpResponse(t.render())