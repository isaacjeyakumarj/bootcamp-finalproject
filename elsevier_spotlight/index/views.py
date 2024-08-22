from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')
    #return HttpResponse('this is homepage')
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def categories(request):
    return render(request,'categories.html')

def topblog(request):
    return render(request,'topblog.html')

