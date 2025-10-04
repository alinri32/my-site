from django.shortcuts import render

from django.http import HttpResponse , JsonResponse

def index_view(request):
    return render(request , '../templates/website/index.html')

def about_view(request):
    return render(request, '../templates/website/about.html')

def contact_view(request):
    return render(request, '../templates/website/contact.html')

def elements_view(request):
    return render(request, '../templates/website/elements.html')