from django.db import models

# I use this model to store one movie that people can book.
class Movie(models.Model):
    # I want a short title for the movie.
    title = models.CharField(max_length=200)
    # I also want a longer description; it’s optional so I allow blank.
    description = models.TextField(blank=True)
    # I’m keeping the release date as a real date.
    release_date = models.DateField()
    # I’m saving the duration in minutes (e.g., 120).
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    # When Django prints a Movie, I just want to see the title.
    def __str__(self):
        return self.title


# This model is for seats for a specific movie.
class Seat(models.Model):
    # I tie each seat to a movie so "A1" is unique per movie, not globally.
    movie = models.ForeignKey(Movie, related_name="seats", on_delete=models.CASCADE)
    # This is the seat label I’ll show to users (like A1, B3, etc).
    seat_number = models.CharField(max_length=10)
    # I track whether the seat is already booked.
    is_booked = models.BooleanField(default=False)

    class Meta:
        # I want each seat_number to appear only once per movie.
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "seat_number"], name="unique_seat_per_movie"
            )
        ]

    # When Django prints a Seat, I want "Movie Title - A1".
    def __str__(self):
        return f"{self.movie.title} - {self.seat_number}"


# This model records one booking that a user makes for a specific seat.
class Booking(models.Model):
    # I keep a link to the movie so I can show it in booking history.
    movie = models.ForeignKey(Movie, related_name="bookings", on_delete=models.CASCADE)
    # I also link to the seat that was booked.
    seat = models.ForeignKey(Seat, related_name="bookings", on_delete=models.CASCADE)
    # For HW2 I’m not wiring up auth yet, so I’ll just store the user’s name.
    user = models.CharField(max_length=100)
    # I want to automatically track when the booking happened.
    booking_date = models.DateTimeField(auto_now_add=True)

    # I’m not making a DB-level unique rule here because I want a history;
    # I’ll block double-booking in the API logic later.

    # When Django prints a Booking, I want: "Alice → MovieTitle A1".
    def __str__(self):
        return f"{self.user} → {self.movie.title} {self.seat.seat_number}"
