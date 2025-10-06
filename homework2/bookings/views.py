from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


# wants full CRUD for movies, so I use a DRF ModelViewSet.
class MovieViewSet(viewsets.ModelViewSet):
    # returns all movies, ordered by id so they’re stable.
    queryset = Movie.objects.all().order_by("id")
    # This line uses my MovieSerializer to convert rows to JSON.
    serializer_class = MovieSerializer


# I uses this viewset for seat info and for booking a specific seat.
class SeatViewSet(viewsets.ModelViewSet):
    # I prefetch the related movie so list/detail calls are efficient.
    queryset = Seat.objects.select_related("movie").all().order_by("id")
    # serializes seats with my SeatSerializer.
    serializer_class = SeatSerializer

    # added a custom POST /api/seats/{id}/book/ endpoint to book a seat.
    @action(detail=True, methods=["post"])
    def book(self, request, pk=None):
        # grabs the seat I’m trying to book.
        seat = self.get_object()

        # reads a simple "user" string from the request body (no auth for HW2).
        user = request.data.get("user", "").strip()
        # makes sure a user name was provided.
        if not user:
            return Response({"detail": "user is required"},
                            status=status.HTTP_400_BAD_REQUEST)

        # blocks booking if the seat is already taken.
        if seat.is_booked:
            return Response({"detail": "seat already booked"},
                            status=status.HTTP_400_BAD_REQUEST)

        # here it marks the seat as booked and saves it.
        seat.is_booked = True
        seat.save(update_fields=["is_booked"])

        # creates a Booking record tied to this seat and movie.
        booking = Booking.objects.create(movie=seat.movie, seat=seat, user=user)

        # returns the new booking as JSON with a 201 status.
        data = BookingSerializer(booking).data
        return Response(data, status=status.HTTP_201_CREATED)


# lets users list booking history and create new bookings directly.
class BookingViewSet(viewsets.ModelViewSet):
    # selects related fields so JSON has what it needs without extra queries.
    queryset = Booking.objects.select_related("movie", "seat").all().order_by("-booking_date")
    # serializes bookings with my BookingSerializer.
    serializer_class = BookingSerializer

    # here it allows filtering by user via ?user=Name to see just that user’s history.
    def get_queryset(self):
        # starts with the base queryset.
        qs = super().get_queryset()
        # this line looks for a user query param and filter if present.
        user = self.request.query_params.get("user")
        if user:
            qs = qs.filter(user=user)
        # returns the filtered or unfiltered queryset.
        return qs

    # overrides create to prevent double-booking if someone posts directly here.
    def create(self, request, *args, **kwargs):
        # pulls out required fields from the request.
        movie_id = request.data.get("movie")
        seat_id = request.data.get("seat")
        user = request.data.get("user", "").strip()

        # makes sure all required inputs are present.
        if not (movie_id and seat_id and user):
            return Response({"detail": "movie, seat, and user are required"},
                            status=status.HTTP_400_BAD_REQUEST)

        # loads the seat and verifies it belongs to the given movie.
        try:
            seat = Seat.objects.select_related("movie").get(id=seat_id)
        except Seat.DoesNotExist:
            return Response({"detail": "seat not found"}, status=status.HTTP_404_NOT_FOUND)

        # checks that the seat’s movie matches the movie id provided.
        if str(seat.movie_id) != str(movie_id):
            return Response({"detail": "seat does not belong to the given movie"},
                            status=status.HTTP_400_BAD_REQUEST)

        # I do not allow double-booking the seat.
        if seat.is_booked:
            return Response({"detail": "seat already booked"},
                            status=status.HTTP_400_BAD_REQUEST)

        # marks the seats as booked and saves.
        seat.is_booked = True
        seat.save(update_fields=["is_booked"])

        # I created the booking record.
        booking = Booking.objects.create(movie_id=movie_id, seat=seat, user=user)

        # Here it serializes the new booking and returns 201.
        serializer = self.get_serializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
