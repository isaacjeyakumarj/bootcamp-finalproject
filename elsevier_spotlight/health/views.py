from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import healthblog

def health(request):
    healthblogdata=healthblog.objects.all()
    context={
        'health':healthblogdata
    }
    return render(request,'health/health.html',context)
    # return HttpResponse('this is aboutpage')
