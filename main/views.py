from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def charge(request):
    return 

def success(request):
    return render(request,'main/success.html')