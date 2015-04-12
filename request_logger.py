class RequestLogger(object):

	def process_request(self, request):
		syslog.syslog(' '.join([request.META['remote_addr'], request.get_full_path(), '\n']))