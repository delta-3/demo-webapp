from django.shortcuts import render
from forms import *
from django.forms.formsets import formset_factory
from delta3.models import Gif, User
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.db import connection, transaction
import logging
logger = logging.getLogger(__name__)

def home(request):
	return render(request, 'delta3/login.html')
	
def login(request):
	# Check if username matches password
	if request.REQUEST.get('username') and request.REQUEST.get('password'):
		un = request.REQUEST.get('username')
		pwd = request.REQUEST.get('password')
		sql = 'SELECT * from delta3_user where username=' + '"' + un + '"' + ' and password=' + '"' + pwd + '"' 
		logger.debug("sql = ..." + sql)        
		users = User.objects.raw(sql)        
		if len(list(users)) > 0:
			# login(request, user)
			return render(request, 'delta3/search.html', {'form': SearchForm})
	return render(request, 'delta3/login.html', {'form': LoginForm})

def comments(request):
	return render(request, 'delta3/comments.html', {'form': CommentsForm})

def search(request):
	if request.method == 'POST':
		if(request.REQUEST.get('searchterm')):
			searchterm = str(request.REQUEST.get('searchterm'))
			sql = 'SELECT * from delta3_gif where gif_name=' + '"' + searchterm + '"' 
			g = Gif.objects.raw(sql)
			# g = Gif.objects.raw('SELECT * from delta3_gif where gif_name=""; SELECT * from delta3_user')
			if len(list(g)) > 0:
				response = ""
				# html = ""
				# for x in g:	
				# 	response = response + str(x) + "<br>"
				# 	url = str(x.gif_url)
				# 	html = html + '<img src="' + url + '"\><br>'
			return render(request, 'delta3/search.html',{'gifs': g, 'query': sql,})
				# return HttpResponse(html)
	# cursor = connection.cursor()
	# cursor.execute('select * from delta3_gif; show tables;')

	return render(request, 'delta3/search.html', {'form': SearchForm})

def about(request):
	return render(request, 'delta3/about.html')

def register(request):
	# Exceptions are manually being created for POC
	# These exceptions will handled by the middlewares.py's "process_exception"
	# Raise ValueError exception if a digit is in firstname or lastname
	if request.REQUEST.get('password') and request.REQUEST.get('username'):
		
		firstname_in = request.REQUEST.get('firstname')
		if any(char.isdigit() for char in firstname_in):
			raise ValueError("Integer detected in firstname in /delta3/register")
		
		lastname_in = request.REQUEST.get('lastname')
		if any(char.isdigit() for char in lastname_in):
			raise ValueError("Integer detected in lastname in /delta3/register")
		
		age_in = int(request.REQUEST.get('age'))
		un_in = request.REQUEST.get('username')
		pwd_in = request.REQUEST.get('password')
		
		#save new user in database
		sql = 'SELECT * from delta3_user where username=' + '"' + un_in + '"' 
		logger.debug("sql = ..." + sql)        
		users = User.objects.raw(sql)        
		if len(list(users)) <= 0:
			sql = 'INSERT INTO delta3_user (username, password) VALUES(' + '"' + un_in + '",' + '"' + pwd_in + '"' + ')' 
			cursor = connection.cursor()
			cursor.execute(sql)
			#transaction.commit_unless_managed()
			logger.debug("sql = ..." + sql)        
			return render(request, 'delta3/login.html')
		else:
			logger.debug("username already exists")        
	return render(request, 'delta3/register.html', {'form': RegisterForm})
