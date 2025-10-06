from django.test import TestCase
from rest_framework.test import APIClient
from bookings.models import Movie, Seat, Booking

class ApiFlowTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_movie_seat_and_book_via_api(self):
        res = self.client.post("/api/movies/", {
            "title": "Interstellar",
            "description": "Space + time",
            "release_date": "2014-11-07",
            "duration": 169,
        }, format="json")
        self.assertEqual(res.status_code, 201)
        movie_id = res.data["id"]

        res = self.client.post("/api/seats/", {
            "movie": movie_id, "seat_number": "A1", "is_booked": False
        }, format="json")
        self.assertEqual(res.status_code, 201)
        seat_id = res.data["id"]

        res = self.client.post(f"/api/seats/{seat_id}/book/", {"user": "Alice"}, format="json")
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["seat"], seat_id)
        self.assertEqual(res.data["movie"], movie_id)

        res = self.client.get(f"/api/seats/{seat_id}/")
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.data["is_booked"])

        res = self.client.post(f"/api/seats/{seat_id}/book/", {"user": "Bob"}, format="json")
        self.assertEqual(res.status_code, 400)

        res = self.client.get("/api/bookings/?user=Alice")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["seat"], seat_id)
