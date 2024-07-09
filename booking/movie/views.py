# movie/views.py

from django.shortcuts import render
from .models import Movie, Booking

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movie/movie_detail.html', {'movie': movie})

def book_tickets(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        num_tickets = int(request.POST.get('num_tickets'))
        user = request.user  # Assuming user is authenticated
        booking = Booking.objects.create(movie=movie, user=user, num_tickets=num_tickets)
        # Additional logic like payment integration can be added here
        return render(request, 'movie/booking_success.html', {'booking': booking})
    return render(request, 'movie/book_tickets.html', {'movie': movie})
