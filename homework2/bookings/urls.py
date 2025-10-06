# homework2/bookings/urls.py

# I need path/include for normal Django URLs and the DRF router for API endpoints.
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# I import my API viewsets and the three simple UI views.
from .views import (
    MovieViewSet,       # /api/movies/...
    SeatViewSet,        # /api/seats/...
    BookingViewSet,     # /api/bookings/...
    movie_list_view,    # /api/ui/
    seat_booking_view,  # /api/ui/movies/<id>/book/
    booking_history_view,  # /api/ui/history/
)

# I set up a DRF router so I don’t have to write all the CRUD URLs by hand.
router = DefaultRouter()
# This registers full CRUD for movies at /api/movies/ (list, create, detail, update, delete).
router.register(r"movies", MovieViewSet, basename="movie")
# Same idea for seats: /api/seats/ (plus my custom POST /api/seats/<id>/book/ action).
router.register(r"seats", SeatViewSet, basename="seat")
# And bookings: /api/bookings/ (list + create; I added logic to prevent double-booking).
router.register(r"bookings", BookingViewSet, basename="booking")

# These are my human-facing pages (Bootstrap templates), kept under /api/ui/ so they
# don’t collide with the API endpoints above.
urlpatterns = [
    # Movie list page. Simple page that links to booking pages for each movie.
    path("ui/", movie_list_view, name="movie_list"),

    # Seat booking page for a specific movie. Shows seats and a tiny form to book one.
    path("ui/movies/<int:movie_id>/book/", seat_booking_view, name="book_seat"),

    # Booking history page. Supports an optional ?user=Alice filter in the query string.
    path("ui/history/", booking_history_view, name="booking_history"),

    # Finally, I mount all the router-generated API URLs (movies, seats, bookings).
    path("", include(router.urls)),
]
