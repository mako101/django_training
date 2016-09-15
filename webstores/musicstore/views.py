from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'musicstore/index.html')


def upload(request):
    genres = Genre.objects.order_by('name')
    #categories = Category.objects.order_by('name')
    categories = Category.objects.all()  # lets try an unordered list
    context = {
        'genres': genres,
        'categories': categories
    }
    return render(request, 'musicstore/upload.html', context)


def browse(request):
    return HttpResponse('<h3>Browse songs here<h3>')
