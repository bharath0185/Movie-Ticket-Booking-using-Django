# movie/models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    num_tickets = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} booked {self.num_tickets} tickets for {self.movie.title} on {self.booking_date}"

# movie/models.py

from django.db import models
from .models import Movie  # Import Movie model if needed

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screening_date = models.DateField()
    screening_time = models.TimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.movie.title} Screening at {self.location} on {self.screening_date}"
