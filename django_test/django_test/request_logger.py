'''
Middleware that records all requests made in a log file

References:
[1] http://stackoverflow.com/questions/4839297/is-there-a-django-middleware-plugin-that-logs-all-my-requests-in-a-organized-fas
'''

class RequestLogger(object):
	# def process_request(self, request):
	# 	with open('requests.log', 'w+') as log_file:
	# 		log_file.write(request.META['remote_addr'] + ": " + request.get_full_path() + "\n")
    def process_request(self, request):
        syslog.syslog(' '.join([ request.META['remote_addr'], request.get_full_path(),]))