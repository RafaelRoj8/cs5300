from django.test import TestCase
from django.db import IntegrityError, transaction
from django.utils import timezone
from bookings.models import Movie, Seat, Booking

class ModelBasicsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(
            title="Inception",
            description="Dream heist",
            release_date="2010-07-16",
            duration=148,
        )

    def test_create_and_fetch_seats(self):
        Seat.objects.create(movie=self.movie, seat_number="A1", is_booked=False)
        Seat.objects.create(movie=self.movie, seat_number="A2", is_booked=False)
        self.assertEqual(self.movie.seats.count(), 2)

    def test_unique_seat_number_per_movie(self):
        Seat.objects.create(movie=self.movie, seat_number="A1", is_booked=False)
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Seat.objects.create(movie=self.movie, seat_number="A1", is_booked=False)

    def test_booking_sets_timestamp(self):
        seat = Seat.objects.create(movie=self.movie, seat_number="B1", is_booked=False)
        booking = Booking.objects.create(movie=self.movie, seat=seat, user="Alice")
        self.assertIsNotNone(booking.booking_date)
        delta = timezone.now() - booking.booking_date
        self.assertLess(delta.total_seconds(), 5.0)
