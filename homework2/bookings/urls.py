# bookings/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MovieViewSet, SeatViewSet, BookingViewSet,
    movie_list_view, seat_booking_view, booking_history_view,
)

router = DefaultRouter()
router.register(r"movies",   MovieViewSet,   basename="movie")
router.register(r"seats",    SeatViewSet,    basename="seat")
router.register(r"bookings", BookingViewSet, basename="booking")

urlpatterns = [
    path("ui/", movie_list_view, name="movie_list"),
    path("ui/movies/<int:movie_id>/book/", seat_booking_view, name="book_seat"),
    path("ui/history/", booking_history_view, name="booking_history"),
    path("", include(router.urls)),
]


