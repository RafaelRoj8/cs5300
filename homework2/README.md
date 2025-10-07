# Homework 2 — Movie Theater Booking (Django + DRF)
## What this does
- REST API to list movies, manage seats, and create bookings
- Simple Bootstrap UI for the same data (movie list, seat booking, booking history)

## Run (DevEdu)
1) Start the server:

```bash
cd ~/cs5300/homework2
source myenv/bin/activate
python manage.py migrate
python manage.py runserver 0.0.0.0:3000
```

## Open the App URLs (recommended):
Movie list:
Seat booking (example id=1):
Booking history:

## API endpoints
GET/POST /api/movies/
GET/POST /api/seats/
POST /api/seats/{id}/book/ (JSON: {"user":"Alice"})
GET/POST /api/bookings/ (prevents double-booking)

## Tests:
```bash
cd ~/cs5300/homework2
source myenv/bin/activate
python manage.py test bookings -v 2
```

## Deployment:
-Repo includes:

-render.yaml (with rootDir: homework2)

-build.sh (collectstatic + migrate)

-requirements.txt

-Production settings (WhiteNoise + dj-database-url) in movie_theater_booking/settings.py

# On Render:

Create a Blueprint from this repo (or manual web service)

Env vars: DATABASE_URL (from Render Postgres), SECRET_KEY (generate), WEB_CONCURRENCY=4

## GitHub:
https://github.com/RafaelRoj8/cs5300/commits/main/homework2


## AI Usage (required):
I used ChatGPT (GPT-5 Thinking) to help fix CSRF/proxy issues, prepare deployment files like render.yaml, build.sh. All code was reviewed and run in DevEdu.


