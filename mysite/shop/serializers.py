from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'




class UserProfileSimplSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields =['first_name', 'last_name']



class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']

class CountrySimplSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name', 'id']






class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields =['director_name']




class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']




class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['Gere_name']


class MovieLanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['video', 'language', 'id']


class MomentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']

class MovieSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['movie_name']



class RatingSerializers(serializers.ModelSerializer):
    user =UserProfileSimplSerializers()
    movie =MovieSerializers()
    class Meta:
        model = Rating
        fields = ['created_date', 'text', 'stars', 'movie', 'user']


class RatingCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'




class RatingSimplSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['stars']





class MovieListSerializers(serializers.ModelSerializer):
    genre = GenreSerializers(read_only=True, many=True)
    get_avg_rating =serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['id','movie_name', 'movie_image', 'genre',  'get_avg_rating']

    def get_avg_rating(self,obj):
         return obj.get_avg_rating()



class MovieDataiSerializers(serializers.ModelSerializer):
    genre =GenreSerializers(many=True, read_only=True)
    actor =ActorSerializers(many=True, read_only=True)
    country =CountrySerializers(many=True,read_only=True)
    director =DirectorSerializers(many=True, read_only=True)
    movies_languages =MovieLanguagesSerializers(many=True, read_only=True)
    moments_movie =MomentsSerializers(many=True, read_only=True)
    rating_movie =RatingSerializers(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['movie_image', 'movie_trailer', 'description', 'movie_time',
                  'types', 'genre', 'actor', 'director', 'country', 'year',
                  'movie_name', 'movies_languages', 'moments_movie',
                  'rating_movie', 'get_avg_rating']

    def get_avg_rating(self,obj):
        return obj.get_avg_rating()


class CountryDataiSerializers(serializers.ModelSerializer):
    country_movie = MovieDataiSerializers(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['country_movie']

class ActorSimplSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name', 'id']


class ActorDataiSerializers(serializers.ModelSerializer):
    actor_movie = MovieDataiSerializers(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ['actor_movie']



class DirectorSimplSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields =['director_name', 'id']


class DirectorDataiSerializers(serializers.ModelSerializer):
    director_movie = MovieDataiSerializers(many=True, read_only=True)
    class Meta:
        model = Director
        fields = ['director_movie']


class GenreSimplSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['Gere_name', 'id']


class GenreDataiSerializers(serializers.ModelSerializer):
    gener_movie = MovieDataiSerializers(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['gener_movie']


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'




class FavoriteMovieSerializers(serializers.ModelSerializer):
    user=UserProfileSerializers(many=True, read_only=True)
    class Meta:
        model = FavoriteMovie
        fields ='__all__'



class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


class MovieLanguagesSimplSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'id']



class MovieLanguagesDataiSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['video', 'language', 'id']








