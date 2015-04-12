'''
Middleware that logs all requests

References:
[1] http://stackoverflow.com/questions/4839297/is-there-a-django-middleware-plugin-that-logs-all-my-requests-in-a-organized-fas
'''

class RequestLogger(object):

	def process_request(self, request):
		syslog.syslog(' '.join([request.META['remote_addr'], request.get_full_path(), '\n']))