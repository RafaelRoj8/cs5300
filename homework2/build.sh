#!/usr/bin/env bash
set -o errexit

# Install deps for the build
pip install -r requirements.txt

# Collect static files for WhiteNoise (only actually served when DEBUG=False on Render)
python manage.py collectstatic --no-input

# Apply DB migrations
python manage.py migrate
