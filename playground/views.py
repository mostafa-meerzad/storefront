from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def say_hello(request):
    # return HttpResponse("Hello World")
    # return render(request, "hello.html") # render template with no dynamic data provided
    return render(request, "hello.html", {"name": "Mostafa"}) # name is provided as dynamic data
