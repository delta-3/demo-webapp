from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
from polls.models import Poll


# Create your views here.
def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('polls/index.html')
   	c = Context({ 'latest_poll_list': latest_poll_list,})
   	f = open('/home/ddortega/Desktop/request-logger/django_test/requests.log','a')
	f.write(str(request.get_host()) + str(request.get_full_path()) + str(request.REQUEST) + "\n") 
	# f.write(str(request.POST) + "\n") 
	f.close() 
	return HttpResponse(t.render(c))

# def detail(request, poll_id):
def detail(request):
	# return HttpResponse("You're looking at poll details%s." % poll_id)
	return HttpResponse("You're looking at poll details" % poll_id)

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)
