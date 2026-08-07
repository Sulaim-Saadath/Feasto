from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    # return HttpResponse("Say hello my app is working!")
    return render(request, "index.html")