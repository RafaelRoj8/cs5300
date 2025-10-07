# I import Django’s TestCase to get a fresh test database for each test class.
from django.test import TestCase
# I need IntegrityError to assert my uniqueness constraint fails on duplicates.
from django.db import IntegrityError, transaction
# I’ll check that the booking_date is set close to “now”.
from django.utils import timezone

# I import my three models to create and query data.
from bookings.models import Movie, Seat, Booking


# I group my model tests in a class so setUpTestData can seed once per class.
class ModelBasicsTests(TestCase):
    # I create one movie that all tests in this class can reuse.
    @classmethod
    def setUpTestData(cls):
        # I make a movie record to attach seats/bookings to.
        cls.movie = Movie.objects.create(
            title="Inception",
            description="Dream heist",
            release_date="2010-07-16",
            duration=148,
        )

    # I verify I can create seats for my movie and fetch them back.
    def test_create_and_fetch_seats(self):
        # I create two seats for the same movie.
        Seat.objects.create(movie=self.movie, seat_number="A1", is_booked=False)
        Seat.objects.create(movie=self.movie, seat_number="A2", is_booked=False)
        # I count how many seats this movie has (should be 2).
        count = self.movie.seats.count()
        # I assert the count is exactly 2.
        self.assertEqual(count, 2)

    # I assert the (movie, seat_number) pair is unique (as per my model constraint).
    def test_unique_seat_number_per_movie(self):
        # I create the first seat with number A1 for this movie.
        Seat.objects.create(movie=self.movie, seat_number="A1", is_booked=False)
        # I try to create a duplicate A1 seat for the same movie.
        with self.assertRaises(IntegrityError):
            # I wrap it in a transaction so the test can catch the DB error cleanly.
            with transaction.atomic():
                Seat.objects.create(movie=self.movie, seat_number="A1", is_booked=False)

    # I check that booking_date is automatically set when I create a Booking.
    def test_booking_sets_timestamp(self):
        # I make a free seat to book.
        seat = Seat.objects.create(movie=self.movie, seat_number="B1", is_booked=False)
        # I create a booking row (note: model doesn’t auto-toggle is_booked).
        booking = Booking.objects.create(movie=self.movie, seat=seat, user="Alice")
        # I assert that booking_date is not None and is very close to now.
        self.assertIsNotNone(booking.booking_date)
        # I compute the time delta from now to booking time.
        delta = timezone.now() - booking.booking_date
        # I assert the delta is small (a few seconds).
        self.assertLess(delta.total_seconds(), 5.0)
