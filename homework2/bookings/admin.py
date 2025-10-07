# I’m using Django’s admin so I can add and view data quickly in /admin/.
from django.contrib import admin

# I import my three models so I can register them with the admin site.
from .models import Movie, Seat, Booking

# I want Movie to show up in the admin.
admin.site.register(Movie)

# I want Seat to show up in the admin.
admin.site.register(Seat)

# I want Booking to show up in the admin.
admin.site.register(Booking)

