from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.

# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
#     domain=None, secure=None, httponly=False, samesite=None)
def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get("zap", None)
    resp = HttpResponse("In a view - the zap cookie value is " + str(oldval))
    if oldval:
        resp.set_cookie("zap", int(oldval) + 1)  # No expired date = until browser close
    else:
        resp.set_cookie("zap", 42)  # No expired date = until browser close
    resp.set_cookie("sakaicar", 42, max_age=1000)  # seconds until expire
    return resp


# https://www.youtube.com/watch?v=Ye8mB6VsUHw


def sessfun(request):
    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits
    if num_visits > 4:
        del request.session["num_visits"]
    resp = HttpResponse("view count=" + str(num_visits))
    resp.set_cookie("dj4e_cookie", "0d730fb2", max_age=1000)
    return resp


''' from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.


def helloworld(request):
    logging.error("Hello world DJ4E in the log...")
    print("Hello world DJ4E in a print statement...")
    response = """<html><body><p>Hello world DJ4E in HTML</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    return HttpResponse(response) '''
