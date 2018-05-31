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
    return render(request, 'all/index.html', {"events": events, "news": news, "testimonials": testimonials, "service": service})


def news(request, news_id):
    try:
        news = News.objects.get(id=news_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all/news.html", {"news": news})
