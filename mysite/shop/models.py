from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import  MinValueValidator, MaxValueValidator

STATUS_CHOICES=(
        ('pro',   'pro'),
        ('simple',  'simple')
    )


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(16),   MaxValueValidator(100)
    ],null=True, blank=True)

    status= models.CharField(choices=STATUS_CHOICES,max_length=45, default='simple')

    def __str__(self):
        return f'{self.username}'

class Country(models.Model):
   country_name= models.CharField(max_length=46, unique=True)

   def __str__(self):
       return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=86)
    bio = models.TextField()
    age = models.IntegerField()
    director_image = ImageField(upload_to='directors_image/')

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name=models.CharField(max_length=78)
    bio = models.TextField()
    age = models.IntegerField()
    actor_image = models.ImageField(upload_to='actors_image/')

    def __str__(self):
        return self.actor_name

class Genre(models.Model):
    Gere_name = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.Gere_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=99)
    year = models.IntegerField()
    country = models.ManyToManyField(Country, related_name='country_movie')
    director = models.ManyToManyField(Director, related_name='director_movie')
    actor = models.ManyToManyField(Actor, related_name='actor_movie')
    genre = models.ManyToManyField(Genre, related_name='gener_movie')
    TYPE_CHOICES=(
        ('144', '144'),
        ('360', '360'),
        ('480', '480'),
        ('720', '720'),
        ('1080', '1080')
    )
    types =models.CharField(choices=TYPE_CHOICES, max_length=45)
    movie_time = models.DateField()
    description = models.TextField(verbose_name='отисания_филма')
    movie_trailer = models.FileField(upload_to=' movies_trailer/')
    movie_image = models.ImageField(upload_to='movies_image/')

    status_movie = models.CharField(choices=STATUS_CHOICES,max_length=45)

    def __str__(self):
        return f'{self.movie_name}'

    def get_avg_rating(self):
       totol = self.rating_movie.all()
       if totol.exists():
           return round(sum([i.stars for i in totol]) /  totol.count(), 1)

       return 0






class MovieLanguages(models.Model):
    language = models.CharField(max_length=87)
    video = models.FileField(upload_to='videos/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies_languages')

    def __str__(self):
        return f'{self.language}'



class Moments(models.Model):
  movie= models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moments_movie')
  movie_moments= models.ImageField(upload_to='movies_moments/')

  def __str__(self):
      return f'{self.movie_moments}'



class Rating(models.Model):
    user =models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rating_movie')
    stars =models.IntegerField(choices=[(i,  str(i))for i in range(1, 11)])
    text=models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.movie}, {self.stars}'



class Favorite(models.Model):
    user=models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}'


class FavoriteMovie(models.Model):
    cart= models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cart}, {self.movie}'



class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie =models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user}, {self.movie}, {self.viewed_at}'

