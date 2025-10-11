from django.shortcuts import render
from blog.models import post , Category
from django.http import HttpResponse , JsonResponse , HttpResponseRedirect
from website.forms import contactform , newsletterform

def index_view(request):
    posts = post.objects.filter(status = 1).order_by('-published_date')[:4]
    context = {'posts':posts}
    return render(request , '../templates/website/index.html',context)

def about_view(request):
    return render(request, '../templates/website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
    
    form = contactform()
    
    return render(request, '../templates/website/contact.html',{'form':form})

def elements_view(request):
    return render(request, '../templates/website/elements.html')

def newsletter_view(request):
    if request.method == 'POST':
        print('pst')
        form = newsletterform(request.POST)
        if form.is_valid():
            print('post')
            form.save()
            HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
    return HttpResponseRedirect('/')