# movie/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:movie_id>/book_tickets/', views.book_tickets, name='book_tickets'),
    # Add other URL patterns as needed
]
