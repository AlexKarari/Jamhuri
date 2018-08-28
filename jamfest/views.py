from django.shortcuts import render, redirect
from .models import Artist, Events, Articles, Releases, Merchandise, Testimonials, Services, NewsLetterRecipients
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .filters import ArtistFilter
from .forms import NewsLetterForm

# Create your views here.

def index(request):
    '''
    View function that displays the homepage and all its contents.
    Most content here acts as links to the main content.
    '''
    events = Events.objects.all()[0:3]
    article = Articles.objects.all()[0:3]
    testimonials = Testimonials.objects.all()
    service = Services.objects.all()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            HttpResponseRedirect('landingpage')
    else:
        form = NewsLetterForm()
    return render(request, 'all/index.html', {"events": events, "article": article, "testimonials": testimonials, "service": service, "letterForm": form})


def all_artists(request):
    '''
    View function that displays all artists in the company's agency and a search criteria for them
    '''
    bTitle = 'jamhuri Artists'
    link = 'Artists'
    artists = Artist.objects.all()
    artist_filter = ArtistFilter(request.GET, queryset=artists)
    return render(request, 'all/allartists.html', {"artists": artists, "artist_filter": artist_filter,'bTitle':bTitle,'link':link})



def single_artist(request, artist_id):
    bTitle = 'Artist Profile'
    
    artists = Artist.objects.get(pk=artist_id)
    link = artists.name
    return render(request, "all/single_artist.html", {"artists": artists,'bTitle':bTitle,'link':link})

def articles(request, article_id):
    try:
        article = Articles.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()
    bTitle = article.title
    link = article.title
    articles = Articles.objects.all()[0:4]
    return render(request, "all/articles.html", {"article": article,'bTitle':bTitle,'link':link,'articles':articles})

def shows(request, events_id):
    events = Events.objects.get(pk=events_id)
    return render(request, "all/shows.html", {"events": events})


def search_results(request):
    '''
    View function that enables a user search for any artist in the agency
    '''

    if 'artist' in request.GET and request.GET["artist"]:
        search_term = request.GET.get("artist")
        searched_artist = Artist.search_by_name(search_term)
        message = f"{search_term}"
        bTitle = 'Artist Search Results'
        link = 'Search'

        return render(request, 'all/search.html', {"message": message, "searched_artist": searched_artist,'bTitle':bTitle,'link':link})

    else:
        message = "You are yet to search for an artist"
        return render(request, 'all/search.html', {"message": message})


def about(request):
    '''
    View function that displays what the company's agency is all about
    '''
    bTitle = 'About Jamhuri'
    link = 'About'
    return render(request, 'all/about.html',{'link':link,'bTitle':bTitle})
    


def all_shows_list(request):
    '''
    view function to display all the shows for jamhuri events
    '''
    events = Events.objects.all()
    return render(request, 'all/show_list.html', {"events": events})

def all_articles_list(request):
    '''
    view function to display all Jamhuri's articles
    '''
    bTitle = 'Jamhuri Blog'
    link = 'Blog'
    article = Articles.objects.all()
    return render(request, 'all/articles_list.html', {"article": article,'link':link,'bTitle':bTitle})



def test(request):
    '''
    This view function will render a test page
    '''
    events = Events.objects.all()[0:3]
    article = Articles.objects.all()[0:3]
    testimonials = Testimonials.objects.all()
    service = Services.objects.all()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            HttpResponseRedirect('landingpage')
    else:
        form = NewsLetterForm()
    return render(request, 'test.html', {"events": events, "article": article, "testimonials": testimonials, "service": service, "letterForm": form})