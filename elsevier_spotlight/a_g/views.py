from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def a_g(request):
    return render(request,'a_g/a_g.html')
    # return HttpResponse('this is aboutpage')
