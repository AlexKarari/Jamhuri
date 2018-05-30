from django.shortcuts import render, redirect
from .models import Artist, Events, News, Releases, Merchandise

# Create your views here.


def index(request):
    '''
    View function that displays the homepage and all its contents 
    '''
    events = Events.objects.all()
    return render(request, 'all/index.html', {"events": events})

def events(request):
        '''
        View function that gets all events being advertised
        '''
        return render(request, 'all/index.html')
