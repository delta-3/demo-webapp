from django.shortcuts import render
from forms import *
from django.forms.formsets import formset_factory
from delta3.models import User, Gif, Comment
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.db import connection
from django.template import Context

def home(request):
	return render(request, 'delta3/home.html')
	
def login(request):
	return render(request, 'delta3/login.html', {'form': LoginForm})

def comments(request):
	request_method = request.method
	
	# If GET request, render comments form and clear out comment_display variable
	if (request_method == 'GET'):
		img_left = "http://static.comicvine.com/uploads/original/11111/111112756/3141240-0483057803-Chuck.jpg"
		img_right = "http://4.bp.blogspot.com/_JzInBXovu8w/SfHCOysBbiI/AAAAAAAAAgo/WapyJWFBJz4/s400/chuck-norris.jpg"
		context = {'form': CommentsForm, 'thanks_statement': "", 'all_comments_statement': "", 'img_left': img_left, 'img_right': img_right}
		return render(request, 'delta3/comments.html', context)
	
	# If POST request, 
	elif (request_method == 'POST'):
		# TODO Get username from database and add to Comment Model
		comment = request.POST.get('comment_submit')
		if "script" in comment:
			raise ValueError("XSS detected\n" )
		# Create Comment model and save to database
		#c = Comment(user=username, content=comment)
		c = Comment(content=comment)
		c.save()
		all_comments = Comment.objects.all().order_by('-id') # Most recent first
		thanks_statement = "Thanks for your comment: "
		all_comments_statement = "All comments: "
		img_left = "http://www.clipartbest.com/cliparts/nTX/EB7/nTXEB7jTB.jpeg"
		img_right = "http://media.giphy.com/media/1HrVMip45ciJy/giphy.gif"
		context = {'form': CommentsForm, 'comment_display': comment, 'all_comments': all_comments, 'thanks_statement': thanks_statement, 'all_comments_statement': all_comments_statement, 'img_left': img_left, 'img_right': img_right}
		return render(request, 'delta3/comments.html', context)
		#context = Context({'form': CommentsForm, 'comment_display': comment, 'all_comments': all_comments, 'thanks_statement': thanks_statement, 'all_comments_statement': all_comments_statement, 'img_left': img_left, 'img_right': img_right}, autoescape=False)
		#return render(request, 'delta3/comments.html', context)

def search(request):
	if request.method == 'POST':
		if(request.REQUEST.get('searchterm')):
			searchterm = str(request.REQUEST.get('searchterm'))
			sql = 'SELECT * from delta3_gif where gif_name=' + '"' + searchterm + '"' 
			g = Gif.objects.raw(sql)
			# g = Gif.objects.raw('SELECT * from delta3_gif where gif_name=""; SELECT * from delta3_user')
			if (g):
				response = ""
				html = ""
				for x in g:	
					response = response + str(x) + "<br>"
					url = str(x.gif_url)
					html = html + "<img src=" + url + "\><br>"
				return HttpResponse(html)
	return render(request, 'delta3/search.html', {'form': SearchForm})

def about(request):
	return render(request, 'delta3/about.html')

def register(request):
	# Exceptions are manually being created for POC
	# These exceptions will handled by the middlewares.py's "process_exception"
	# Raise ValueError exception if a digit is in firstname or lastname
	if (request.REQUEST.get('firstname')):
		firstname_in = request.REQUEST.get('firstname')
		if any(char.isdigit() for char in firstname_in):
			raise ValueError("Integer detected in firstname in /delta3/register")

	if (request.REQUEST.get('lastname')):
		lastname_in = request.REQUEST.get('lastname')
		if any(char.isdigit() for char in lastname_in):
			raise ValueError("Integer detected in lastname in /delta3/register")

	# Raise ValueError exception if a character is found in the grad_year
	if(request.REQUEST.get('grad_year')):
		x = int(request.REQUEST.get('grad_year'))
		# try: 
		# 	x = int(request.POST.get('grad_year'))
		# except ValueError:
		# 	return HttpResponse("ValueError exception thrown")
	return render(request, 'delta3/register.html', {'form': RegisterForm})
