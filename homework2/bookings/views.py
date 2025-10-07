# bookings/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


# ======== API (DRF) ========

class MovieViewSet(viewsets.ModelViewSet):
    """Full CRUD for movies at /api/movies/"""
    queryset = Movie.objects.all().order_by("id")
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    """List, create, update seats at /api/seats/ + a custom book action."""
    queryset = Seat.objects.select_related("movie").all().order_by("id")
    serializer_class = SeatSerializer

    @action(detail=True, methods=["post"])
    def book(self, request, pk=None):
        """
        POST /api/seats/{id}/book/  with JSON: {"user":"Alice"}
        Book this seat if available; create a Booking row.
        """
        seat = self.get_object()
        user = (request.data.get("user") or "").strip()
        if not user:
            return Response({"detail": "user is required"},
                            status=status.HTTP_400_BAD_REQUEST)
        if seat.is_booked:
            return Response({"detail": "seat already booked"},
                            status=status.HTTP_400_BAD_REQUEST)

        seat.is_booked = True
        seat.save(update_fields=["is_booked"])
        booking = Booking.objects.create(movie=seat.movie, seat=seat, user=user)
        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)


class BookingViewSet(viewsets.ModelViewSet):
    """List bookings or create at /api/bookings/ (prevents double-booking)."""
    queryset = Booking.objects.select_related("movie", "seat").all().order_by("-booking_date")
    serializer_class = BookingSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.query_params.get("user")
        if user:
            qs = qs.filter(user=user)
        return qs

    def create(self, request, *args, **kwargs):
        movie_id = request.data.get("movie")
        seat_id = request.data.get("seat")
        user = (request.data.get("user") or "").strip()

        if not (movie_id and seat_id and user):
            return Response({"detail": "movie, seat, and user are required"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            seat = Seat.objects.select_related("movie").get(id=seat_id)
        except Seat.DoesNotExist:
            return Response({"detail": "seat not found"}, status=status.HTTP_404_NOT_FOUND)

        if str(seat.movie_id) != str(movie_id):
            return Response({"detail": "seat does not belong to the given movie"},
                            status=status.HTTP_400_BAD_REQUEST)

        if seat.is_booked:
            return Response({"detail": "seat already booked"},
                            status=status.HTTP_400_BAD_REQUEST)

        seat.is_booked = True
        seat.save(update_fields=["is_booked"])
        booking = Booking.objects.create(movie_id=movie_id, seat=seat, user=user)
        return Response(self.get_serializer(booking).data, status=status.HTTP_201_CREATED)


# ======== UI (templates) ========

def movie_list_view(request):
    """Simple Bootstrap page of movies with 'Book Now' links."""
    movies = Movie.objects.all().order_by("id")
    return render(request, "bookings/movie_list.html", {"movies": movies})


def seat_booking_view(request, movie_id: int):
    """
    Shows seats for a movie and processes the simple booking form.
    On success: redirect to booking history (optionally filtered by ?user=...).
    On error: re-render page with an error message.
    """
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie).order_by("seat_number")
    message = None

    if request.method == "POST":
        # Match the template field names exactly:
        seat_number = (request.POST.get("seat_number") or "").strip().upper()
        user = (request.POST.get("user") or "").strip()

        if not seat_number or not user:
            message = "Seat number and your name are required."
        else:
            seat = Seat.objects.filter(movie=movie, seat_number=seat_number).first()
            if not seat:
                message = f'Seat "{seat_number}" does not exist for this movie.'
            elif seat.is_booked:
                message = f'Seat "{seat_number}" is already booked.'
            else:
                seat.is_booked = True
                seat.save(update_fields=["is_booked"])
                Booking.objects.create(movie=movie, seat=seat, user=user)
                return redirect(f"{reverse('booking_history')}?user={user}")

    return render(
        request,
        "bookings/seat_booking.html",
        {"movie": movie, "seats": seats, "message": message},
    )


def booking_history_view(request):
    """List bookings; supports ?user=Alice filter."""
    user = (request.GET.get("user") or "").strip()
    qs = Booking.objects.select_related("movie", "seat").order_by("-booking_date")
    if user:
        qs = qs.filter(user=user)
    return render(request, "bookings/booking_history.html", {"bookings": qs, "user": user})
