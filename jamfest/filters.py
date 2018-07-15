import django_filters
from django import forms
from .models import Artist


class ArtistFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    event = django_filters.CharFilter(lookup_expr='exact'),
    talent = django_filters.CharFilter(lookup_expr='exact'),
    genre = django_filters.CharFilter(lookup_expr='icontains'),
    price_lte = django_filters.NumberFilter(name='price', lookup_expr='lte'),
    class Meta:
        model = Artist
        exclude = ['bio', 'avatar']
