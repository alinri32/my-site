from django.shortcuts import render

# Create your views here.
def blog_view (request):
    return render(request , '../templates/blog/blog-home.html')

def blog_single(request):
    return render(request , '../templates/blog/blog-single.html')