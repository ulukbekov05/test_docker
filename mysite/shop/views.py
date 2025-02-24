from rest_framework import viewsets,  generics, status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *

from .serializers import *
from django_filters .rest_framework import DjangoFilterBackend
from .filters import MovieFilter
from rest_framework .filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from .permissions import CheckStatus

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['movie_name']
    ordering_fields = ['year']


class MovieDataiAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDataiSerializers
    permission_classes =  [CheckStatus]




class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializers

    def get_queryset(self):
        return History.objects.filter(id=self.request.user.id)


class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset =FavoriteMovie .objects.all()
    serializer_class = FavoriteMovieSerializers

    def get_queryset(self):
        return FavoriteMovie.objects.filter(id=self.request.user.id)


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers

def get_queryset(self):
        return Favorite.objects.filter(id=self.request.user.id)


class CountrySimplAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySimplSerializers


class CountryDataiAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDataiSerializers


class DirectorSimplAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSimplSerializers


class DirectorDataiAPIView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDataiSerializers


class ActorSimplAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSimplSerializers


class ActorDataiAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDataiSerializers


class GenreSimplAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSimplSerializers


class GenreDataiAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreDataiSerializers


class MovieLanguagesSimplAPIView(generics.ListAPIView):
    queryset = MovieLanguages.objects.all()
    serializer_class =MovieLanguagesSimplSerializers


class MovieLanguagesDataiAPIView(generics.RetrieveAPIView):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesDataiSerializers


class MomentsVAPIView(generics.ListAPIView):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializers


class RatingCommentAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingCommentSerializers

