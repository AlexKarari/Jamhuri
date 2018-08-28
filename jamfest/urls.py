from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^test$',views.test,name = 'test'),
    url('^$', views.index, name='landingpage'),
    url(r'^article/(\d+)/$', views.articles, name='articles'),
    url(r'^all_artists/$', views.all_artists, name='all_artists'),
    url(r'^solo_artist/(\d+)/$', views.single_artist, name='solo_artist'),
    url(r'^shows/(\d+)/$', views.shows, name='shows'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^about/$', views.about, name='about_us'),
    url(r'^all_shows/$', views.all_shows_list, name='all_shows'),
    url(r'^all_articles/$', views.all_articles_list, name='all_articles'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
