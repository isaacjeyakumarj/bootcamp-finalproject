from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def industry(request):
    return render(request,'industry/industry.html')
    # return HttpResponse('this is aboutpage')
