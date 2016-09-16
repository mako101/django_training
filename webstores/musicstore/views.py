from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    return render(request, 'musicstore/index.html')


def upload(request):
    genres = Genre.objects.order_by('name')
    categories = Category.objects.all()  # lets try an unordered list
    context = {
        'genres': genres,
        'categories': categories
    }
    return render(request, 'musicstore/upload.html', context)


def submit(request):
    """
    DB API query to create a song (required params only)
    song1=Song(title='Booya', artist='Bob', upload_date=timezone.now(),
    genre=Genre(id=2), song_file='songs/booya.mp3')

    Adding a category:
    c=Category.objects.get(id=1)
    song1.categories.all()
    """


    # Dictionary of all song pa


def browse(request):
    return HttpResponse('<h3>Browse songs here<h3>')

