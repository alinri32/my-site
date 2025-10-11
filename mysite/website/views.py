from django.shortcuts import render
from blog.models import post , Category
from django.http import HttpResponse , JsonResponse

def index_view(request):
    posts = post.objects.filter(status = 1).order_by('-published_date')[:4]
    context = {'posts':posts}
    return render(request , '../templates/website/index.html',context)

def about_view(request):
    return render(request, '../templates/website/about.html')

def contact_view(request):
    return render(request, '../templates/website/contact.html')

def elements_view(request):
    return render(request, '../templates/website/elements.html')