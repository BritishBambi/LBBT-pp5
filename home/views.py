from django.shortcuts import render

# Create your views here.


def index(request):
    """ A Simple view to render the home screen """
    return render(request, 'home/index.html')


def about_us(request):
    """ A Simple view to render the about us page """
    return render(request, 'home/about_us.html')
