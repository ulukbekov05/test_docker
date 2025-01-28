from django_filters import FilterSet
from .models import Movie


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields ={
            'country': ['exact'],
            'year':    ['gt', 'lt'],
            'status_movie':  ['exact'],
            'genre':     ['exact'],
            'director':  ['exact'],
            'actor':    ['exact']


        }
