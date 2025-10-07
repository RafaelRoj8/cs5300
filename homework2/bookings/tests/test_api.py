# I use APITestCase or APIClient to hit my DRF endpoints end-to-end.
from django.test import TestCase
from rest_framework.test import APIClient

# I import models in case I need to check DB state directly.
from bookings.models import Movie, Seat, Booking


# I keep my API tests together; setUp creates a fresh API client for each test.
class ApiFlowTests(TestCase):
    # I set up a client I can reuse across methods.
    def setUp(self):
        # I create one DRF APIClient to make HTTP requests in tests.
        self.client = APIClient()

    # I test the main flow: create movie -> create seat -> book seat -> verify.
    def test_create_movie_seat_and_book_via_api(self):
        # ---------- create a movie ----------
        # I POST to /api/movies/ to add a new movie.
        movie_payload = {
            "title": "Interstellar",
            "description": "Space + time",
            "release_date": "2014-11-07",
            "duration": 169,
        }
        # I send JSON and expect a 201 response with an id.
        res = self.client.post("/api/movies/", movie_payload, format="json")
        self.assertEqual(res.status_code, 201)
        movie_id = res.data["id"]

        # ---------- create a seat ----------
        # I add a seat A1 for that movie (is_booked starts as False).
        seat_payload = {"movie": movie_id, "seat_number": "A1", "is_booked": False}
        res = self.client.post("/api/seats/", seat_payload, format="json")
        self.assertEqual(res.status_code, 201)
        seat_id = res.data["id"]

        # ---------- book the seat using the custom action ----------
        # I POST to /api/seats/<id>/book/ with a simple user name.
        res = self.client.post(f"/api/seats/{seat_id}/book/", {"user": "Alice"}, format="json")
        self.assertEqual(res.status_code, 201)
        # I make sure the booking row came back with a matching seat/movie.
        self.assertEqual(res.data["seat"], seat_id)
        self.assertEqual(res.data["movie"], movie_id)

        # ---------- verify the seat is now booked ----------
        # I GET the seat and check is_booked flipped to True.
        res = self.client.get(f"/api/seats/{seat_id}/")
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.data["is_booked"])

        # ---------- double-book should fail ----------
        # I try to book the same seat again and expect a 400 error.
        res = self.client.post(f"/api/seats/{seat_id}/book/", {"user": "Bob"}, format="json")
        self.assertEqual(res.status_code, 400)

        # ---------- booking history filter ----------
        # I list bookings filtered by user=Alice (should be exactly 1).
        res = self.client.get("/api/bookings/?user=Alice")
        self.assertEqual(res.status_code, 200)
        # I expect exactly one booking in the list and that it’s for the right seat.
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["seat"], seat_id)
