from django.shortcuts import render , get_object_or_404
from blog.models import post

# Create your views here.
def blog_view (request):
    posts = post.objects.filter(status = 1)
    context = {'posts':posts}
    return render(request , '../templates/blog/blog-home.html',context)

def blog_single(request, pid):
    posts = get_object_or_404(post , pk=pid , status=1)
    context = {'posts' : posts}
    return render(request , '../templates/blog/blog-single.html',context)

# def test(request,pid):
#     posts = post.objects.get(id=pid)
#     context = {'posts' : posts}
#     return render(request , '../templates/blog/test.html',context)