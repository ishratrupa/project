from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'new_app/index.html')

def contact(request):
    return render(request, 'new_app/contact.html')

def project(request):
    return render(request, 'new_app/projects.html')

def resume(request):
    return render(request, 'new_app/resume.html')

