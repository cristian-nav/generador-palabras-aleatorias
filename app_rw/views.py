from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    request.session['counter'] = 0
    return render(request, "index.html")

def randomWord(request):
    request.session['counter'] += 1
    context = {
        'rw': get_random_string(length=14),
    }
    return render(request, "index.html", context)
