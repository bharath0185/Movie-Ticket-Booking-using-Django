# movie/admin.py

from django.contrib import admin
from .models import Movie, Screening, Booking

admin.site.register(Movie)
admin.site.register(Screening)
admin.site.register(Booking)
