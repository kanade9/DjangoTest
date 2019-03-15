from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    text = {
        'message': 'yeah!!!!!!!',
        'judge': ['good!', 'soso', 'bad', ]
    }
    return render(request, 'bbs/index.html', text)

# Create your views here.
