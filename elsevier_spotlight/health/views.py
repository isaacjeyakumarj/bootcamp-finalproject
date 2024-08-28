from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from django.http import HttpResponse
from .models import healthblog,health1
from .forms import CommentForm
from django.http import JsonResponse
# from .models import Post

def health(request):
    healthblogdata = health1.objects.filter(status=1).order_by('-created_on')
    context={
        'health':healthblogdata
    }
    return render(request,'health/health.html',context)
    # return HttpResponse('this is aboutpage')

# def PostDetail(request,slug):
#     healthblogdata = get_object_or_404(health1, slug=slug)
#     context={
#         'health':healthblogdata
#     }
#     return render(request,'post_detail.html',context)

def PostDetail(request, slug):
    # Fetch the health-related post based on slug
    healthblogdata = get_object_or_404(health1, slug=slug)
    
    # Fetch the post and associated comments
    post = get_object_or_404(health1, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    
    # Handle new comment submission
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to the database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    # Context data for rendering the template
    context = {
        'health': healthblogdata,
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    
    # Render the template with the context
    return render(request, 'health/post_detail.html', context)


def like_post(request, post_id):
    post = get_object_or_404(health1, id=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({'likes': post.likes, 'dislikes': post.dislikes})

def dislike_post(request, post_id):
    post = get_object_or_404(health1, id=post_id)
    post.dislikes += 1
    post.save()
    return JsonResponse({'likes': post.likes, 'dislikes': post.dislikes})

