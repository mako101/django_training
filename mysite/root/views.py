from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root_index(request):
    # return HttpResponse('<h3>You are at the root dir<h3>')
    return render(request, 'root/index.html')
