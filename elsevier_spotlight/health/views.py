from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import healthblog,health1
# from .models import Post

def health(request):
    healthblogdata = health1.objects.filter(status=1).order_by('-created_on')
    context={
        'health':healthblogdata
    }
    return render(request,'health/health.html',context)
    # return HttpResponse('this is aboutpage')

def PostDetail(request,slug):
    healthblogdata = get_object_or_404(health1, slug=slug)
    context={
        'health':healthblogdata
    }
    return render(request,'post_detail.html',context)

# class PostDetail(generic.DetailView):
#     model = health1
#     template_name = 'post_detail.html'
# def post_detail(request):
#     return render(request,'health/post_detail.html')

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'

# class PostDetail(generic.DetailView):
#      model = health1
#      template_name = 'health/post_detail.html'

# class PostDetail(generic.DetailView):
#     model = health1
#     template_name = 'health/post_detail.html'  # Updated template path
#     context_object_name = 'post'