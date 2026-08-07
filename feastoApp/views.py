from django.http import HttpResponse
from django.shortcuts import render

from .models import Customer

# Create your views here.
def login(request):
    # return HttpResponse("Say hello my app is working!")
    return render(request, "index.html")

def open_signup(request):
    return render(request, "signup.html")

def open_signin(request):
    return render(request, "signin.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        try:
            Customer.objects.get(username = username)
            return HttpResponse("Duplicate Username!")
        except:
            Customer.objects.create(
                username = username,
                password = password,
                email = email,
                mobile = mobile,
                address = address,
            )
    return render(request, "signin.html") 

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    try:
        Customer.objects.get(username = username, password = password)
        if username == 'admin':
            return render(request, 'admin_home.html')
        else:
            return render(request, 'customer_home.html')
    except Customer.DoesNotExist:
        return render(request, 'fail.html')