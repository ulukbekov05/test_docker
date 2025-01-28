from .models import Movie,Genre
from modeltranslation.translator import TranslationOptions,register

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description')



@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('Gere_name',)