import django_filters
from django import forms
from .models import Artist


class ArtistFilter(django_filters.FilterSet):
    event = django_filters.CharFilter(lookup_expr='exact'),
    talent = django_filters.CharFilter(lookup_expr='exact'),
    genre = django_filters.CharFilter(lookup_expr='icontains'),
    price = django_filters.NumberFilter()
    price__lte = django_filters.NumberFilter(name='price', lookup__expr='lte'),
    class Meta:
        model = Artist
        exclude = ['name','bio', 'avatar']
