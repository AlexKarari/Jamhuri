from django.shortcuts import render, redirect
from .models import Artist, Events, News, Releases, Merchandise, Testimonials, Services
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def index(request):
    '''
    View function that displays the homepage and all its contents.
    Most content here acts as links to the main content.
    '''
    events = Events.objects.all()
    news = News.objects.all()
    testimonials = Testimonials.objects.all()
    service = Services.objects.all()
    merchs = Merchandise.objects.all()
    return render(request, 'all/index.html', {"events": events, "news": news, "testimonials": testimonials, "service": service, "merchs": merchs})


def all_artists(request):
    '''
    View function that displays all artists in the company's agency
    '''
    artists = Artist.objects.all()
    return render(request, 'all/allartists.html', {"artists": artists})


def single_artist(request, artist_id):
    try:
        artists = Artist.objects.get(id=artist_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all/single_artist.html", {"artists": artists})

def news(request, news_id):
    try:
        news = News.objects.get(id=news_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all/news.html", {"news": news})

# def shows(request, shows_id):
#     try:
#         shows = Events.objects.get(id=shows_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request, "all/shows.html", {"shows": shows})


def search_results(request):
    '''
    View function that enables a user search for any artist in the agency
    '''

    if 'artist' in request.GET and request.GET["artist"]:
        search_term = request.GET.get("artist")
        searched_artist = Artist.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all/search.html', {"message": message, "searched_artist": searched_artist})

    else:
        message = "You are yet to search for an artist"
        return render(request, 'all/search.html', {"message": message})


def about(request):
    '''
    View function that displays what the company's agency is all about
    '''
    return render(request, 'all/about.html')
