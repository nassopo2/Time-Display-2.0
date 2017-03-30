from django.shortcuts import render, HttpResponse
import datetime # importing  Python's datetime library
# Create your views here.
def current_datetime (request):
     now= datetime.datetime.now ()
     html =" <html> <body> It is now %s. </body> </html>" % now
     return HttpResponse (html)

#steps:
# 1. define a function called current_datetime. This is the view function.
# Each view function takes an HttpRequest object as its first parameter, which
# is typically named request.
# 2. We returned  an HttpResponse object that contains the generated response.
# Each view function is responsible for returning an HttpResponse object.
