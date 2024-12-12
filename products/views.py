from django.shortcuts import render

# Create your views here.
def start_page(request):
    return render(request,'base/start.html')

def login_page(request):
    return render(request,'base/login.html')

def base_page(request):
    return render(request,'base/base.html')