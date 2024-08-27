from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
from django.http import HttpResponse
from .models import agblog,ag1

def a_g(request):
    agblogdata=ag1.objects.filter(status=1).order_by('-created_on')

    context1={
        'ag':agblogdata
    }
    return render(request,'a_g/a_g.html',context1)
    # return HttpResponse('this is aboutpage')


def PostDetail(request,slug):
    agblogdata = get_object_or_404(ag1, slug=slug)
    context1={
        'ag':agblogdata
    }
    return render(request,'post_detail_ag.html',context1)
