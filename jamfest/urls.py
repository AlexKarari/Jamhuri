from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$', views.index, name='landingpage'),
    url(r'^news/(\d+)/$', views.news, name='news'),
    url(r'^all_artists/$', views.all_artists, name='all_artists'),
    url(r'^solo_artist/(\d+)/$', views.single_artist, name='solo_artist'),
    # url(r'^events/(\d+)/$', views.shows, name='shows'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^about/$', views.about, name='about_us'),
    url(r'^search_criteria/$', views.artist_list, name='searcher'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
