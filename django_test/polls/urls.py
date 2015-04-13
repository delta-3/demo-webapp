from django.conf.urls import url

from . import views

# Add views for app "polls" here
urlpatterns = [
	# /polls
    url(r'^$', views.home, name='home'),
    # /polls/strings
	url(r'^strings', views.strings, name='strings'),
	# /polls/numbers
	url(r'^numbers', views.numbers, name='numbers'),
	# /polls/about
	url(r'^about', views.about, name='about'),
]