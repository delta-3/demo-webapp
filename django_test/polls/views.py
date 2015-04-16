from django.shortcuts import render
from forms import *
from django.forms.formsets import formset_factory

# TODO Add code to handle GET and POST requests
def home(request):
	return render(request, 'polls/home.html')

def strings(request):
	return render(request, 'polls/strings.html', {'form': StringsForm})

def numbers(request):
	return render(request, 'polls/numbers.html', {'form': NumbersForm})
	
def login(request):
	return render(request, 'polls/login.html', {'form': LoginForm})

def comments(request):
	return render(request, 'polls/comments.html', {'form': CommentsForm})

def about(request):
	return render(request, 'polls/about.html')

def search(request):
	return render(request, 'polls/search.html', {'form': SearchForm})
