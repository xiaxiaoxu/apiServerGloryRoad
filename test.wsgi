import os
print("!!!!!!!!!!!!!!!os.getcwd()2:")
print(os.getcwd())
import sys
flaskPath = 'D:\flask\apiServerGloryRoad'
if flaskPath not in sys.path:
    sys.path.insert(0, 'D:\\flask\\apiServerGloryRoad')
    sys.path.insert(0, 'D:\\flask\\apiServerGloryRoad\\test')
    sys.path.insert(0, 'D:\\flask\\apiServerGloryRoad\\apiServer')
    sys.path.insert(0, 'D:\\flask\\apiServerGloryRoad\\gloryRoadApi')

print("!!!!!!!!!! sys.path:")
print(sys.path)
#from test import app

print("os.getcwd()2" + os.getcwd())
#from test import sayHello
#sayHello()

from gloryRoadApi import app
from apiServer import api

application = app


'''
def application(environ,start_response):
    status = "200 Ok"
    output = b"Hello wsgi"
    response_headers=[('Content-type','text/plain'),('Content-Length',str(len(output)))]
    start_response(status,response_headers)
    return[output]
'''