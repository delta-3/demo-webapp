# Reference: http://stackoverflow.com/a/17777539
import time
from demo_webapp.models import Request

class RequestLoggerMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs): # TODO change this
        response = view_func(request, *view_args, **view_kwargs) # TODO change this
        
        timestamp = str(int(time.time()))
        full_url = str(request.get_host()) + str(request.get_full_path())
        host = str(request.get_host())
        url_path = str(request.get_full_path())
        is_good = True
        
        # Log GET requests
        if request.method == 'GET':
            param_map = request.GET
        # Log POST requests
        if request.method == 'POST':
            param_map = request.POST

        #save to the database
        if len(param_map) != 0 and "delete_selected" not in str(param_map):
            r = Request(timestamp=timestamp, full_url=full_url, host=host, url_path=url_path, is_good=is_good, param_map=param_map)
            r.save()

            # Open request log file
            # f = open('requests.log', 'a')    
            # f.write(timestamp + ";" + full_url + ";" + host + ";" + url_path + ";" + str(is_good) + ";" +  str(param_map) + "\n")
            # f.close()

        return response
