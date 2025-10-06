from rest_framework import serializers
from .models import Movie, Seat, Booking

# I want a serializer that turns Movie rows into JSON (and back if needed).
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "release_date", "duration"]

# I’m using this to represent seats, including which movie a seat belongs to.
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ["id", "movie", "seat_number", "is_booked"]

# This one is for bookings: which movie + seat + the user that booked it.
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "movie", "seat", "user", "booking_date"]
        read_only_fields = ["booking_date"]
