from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def health(request):
    return render(request,'health/health.html')
    # return HttpResponse('this is aboutpage')
