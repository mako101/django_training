from django.http import HttpResponse

def index(request):
    return HttpResponse('<h3>Hello and welcome to the surveys app!<h3>')
