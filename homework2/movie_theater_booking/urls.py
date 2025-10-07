# movie_theater_booking/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # When someone opens the root (like via DevEdu “Open app”), go to the UI list
    path("", RedirectView.as_view(pattern_name="movie_list", permanent=False)),

    path("admin/", admin.site.urls),

    # Include ALL bookings routes (API + UI) under /api/
    path("api/", include("bookings.urls")),
]