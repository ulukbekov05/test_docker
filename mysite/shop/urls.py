from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users',  UserProfileViewSet, basename='user_list')
router.register(r'favorite',  FavoriteViewSet, basename='favorite_list')
router.register(r'favoriteMovie',  FavoriteMovieViewSet, basename='favoriteMovie_list')
router.register(r'history',  HistoryViewSet, basename='history_list')


urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieAPIView.as_view(),   name='movie_list'),
    path('movie/<int:pk>/',   MovieDataiAPIView.as_view(), name='movie_datai'),
    path('comment/', RatingCommentAPIView.as_view(), name='comment_list'),
    path('country/',  CountrySimplAPIView.as_view(),   name='country_movies'),
    path('country/<int:pk>/',   CountryDataiAPIView.as_view(), name='country_movie_list'),
    path('director/',   DirectorSimplAPIView.as_view(),  name='director_list'),
    path('director/<int:pk>/', DirectorDataiAPIView.as_view(), name='director_way'),
    path('actor/',    ActorSimplAPIView.as_view(),   name='actor_list'),
    path('actor/<int:pk>/',   ActorDataiAPIView.as_view(), name='actor_way'),
    path('gener/',   GenreSimplAPIView.as_view(),   name='gener_list'),
    path('gener/<int:pk>/',  GenreDataiAPIView.as_view(),   name='gener_way'),
    path('movieLanguages', MovieLanguagesSimplAPIView.as_view(),   name='movieLanguages_list'),
    path('movieLanguages/<int:pk>/',  MovieLanguagesDataiAPIView.as_view(), name='moviesLanguages_list'),
    path('register/', RegisterView.as_view(),   name='register'),
    path('login/',   LoginView.as_view(),   name='login' ),
    path('logout/',  LogoutView.as_view(),  name='logout')

]

