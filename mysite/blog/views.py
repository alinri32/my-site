from django.shortcuts import render , get_object_or_404
from blog.models import post
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger

# Create your views here.
def blog_view (request,cat_name=None,author_username=None):
    posts = post.objects.filter(status = 1)
    if cat_name!=None:
        posts = post.objects.filter(category__name = cat_name)

    if author_username:
        posts = post.objects.filter(author__username = author_username)

    posts = Paginator(posts , 3)
    try:
        page_num = request.GET.get('page')
        posts = posts.get_page(page_num)
        
    except PageNotAnInteger:
        posts = posts.get_page(1)

    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts':posts}
    return render(request , '../templates/blog/blog-home.html',context)

def blog_single(request, pid):
    posts = get_object_or_404(post , pk=pid , status=1)
    context = {'posts' : posts}
    return render(request , '../templates/blog/blog-single.html',context)

def blog_search(request):
    posts = post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    
    context = {'posts':posts}
    return render(request ,'../templates/blog/blog-home.html',context )
