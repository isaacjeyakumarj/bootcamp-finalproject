from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')
    #return HttpResponse('this is homepage')

def contact(request):
    return render(request,'contact.html')
    #return HttpResponse('this is homepage')

