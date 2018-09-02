import django_filters
from django import forms
from .models import Artist, Talent, Genre, Type_of_Event


class ArtistFilter(django_filters.FilterSet):
    event = django_filters.ModelMultipleChoiceFilter(queryset=Type_of_Event.objects.all(), widget=forms.CheckboxSelectMultiple)
    talent = django_filters.ModelMultipleChoiceFilter(queryset=Talent.objects.all(), widget=forms.CheckboxSelectMultiple)
    genre = django_filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)
    price__lte = django_filters.NumberFilter(name='price', lookup__expr='lte'),
    class Meta:
        model = Artist
        exclude = ['name','bio', 'avatar']
