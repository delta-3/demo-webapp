# Reference: http://stackoverflow.com/a/17777539
import time

class RequestLoggerMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs): # TODO change this
        #response = view_func(request, *view_args, **view_kwargs)
        # Open request log file
        f = open('requests.log', 'a')

        # Log GET requests
        if request.method == 'GET':
            f.write(str(time.strftime("%Y-%m-%d %H:%M:%S")) + ";" + str(request.META["REMOTE_ADDR"]) + ";" + str(request.get_host()) + ";" + str(request.get_full_path()) + ";" + str(request.method) + ";" + str(request.GET) + "\n")
            f.close()

        # Log POST requests
        if request.method == 'POST':
            f.write(str(time.strftime("%Y-%m-%d %H:%M:%S")) + ";" + str(request.META["REMOTE_ADDR"]) + ";" + str(request.get_host()) + ";" + str(request.get_full_path()) + ";" + str(request.method) + ";" + str(request.POST) + "\n")
            f.close()

        return #response