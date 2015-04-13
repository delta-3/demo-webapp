from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse

def index(request):
	t = loader.get_template('polls/index.html') # Load HTML file

   	'''
   	# Moved code to middleware file "request_logger_middleware.py"
   	f = open('/home/minniek/Desktop/github_repos/request-logger/django_test/requests.log', 'a') # Open request log file

   	# Log GET requests
   	if request.method == 'GET':
   		f.write(datetime.datetime.now() + ";" + str(request.META["REMOTE_ADDR"]) + ";" + str(request.get_host()) + ";" + str(request.get_full_path()) + ";" + str(request.GET) + "\n")
		f.close()

	# Log POST requests
   	if request.method == 'POST':
		f.write(str(request.META["REMOTE_ADDR"]) + ";" + str(request.get_host()) + ";" + str(request.get_full_path()) + ";" + str(request.POST) + "\n")
		f.close()
	'''
	return HttpResponse(t.render())
