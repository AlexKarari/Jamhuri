import django_filters
from django import forms
from .models import Artist


class ArtistFilter(django_filters.FilterSet):
    class Meta:
        model = Artist
        fields = ['name', 'event', 'talent', 'genre', 'price']
