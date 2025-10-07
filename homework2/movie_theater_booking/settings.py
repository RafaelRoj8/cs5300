import os
import dj_database_url
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret & Debug:
# - In production (Render), SECRET_KEY comes from env and DEBUG is False.
# - In DevEdu, we fall back to a safe dev default and DEBUG=True.
SECRET_KEY = os.environ.get('SECRET_KEY', default='dev-only-not-secret')
DEBUG = 'RENDER' not in os.environ  # Render sets RENDER=1

# Hosts & CSRF:
# Allow local dev + DevEdu domains. Also trust DevEdu for CSRF over HTTPS.
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.devedu.io']
CSRF_TRUSTED_ORIGINS = ['https://*.devedu.io']

# On Render, add its hostname to allowed hosts + CSRF trusted origins.
RENDER_HOST = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_HOST:
    ALLOWED_HOSTS.append(RENDER_HOST)
    CSRF_TRUSTED_ORIGINS.append(f'https://{RENDER_HOST}')

# Inform Django it's behind a proxy so request.is_secure() is accurate on Render.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'bookings',
]

# Middleware (WhiteNoise immediately after SecurityMiddleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'movie_theater_booking.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # App templates are enough for this project (APP_DIRS=True)
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'movie_theater_booking.wsgi.application'

# Database:
# - On Render, use Postgres from DATABASE_URL (with SSL).
# - Locally, use SQLite.
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# I18N / TZ
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'

# In production (DEBUG=False), collect to staticfiles/ and let WhiteNoise serve them.
if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default PK
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
