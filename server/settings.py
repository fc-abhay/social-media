from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'twitterbackendsecrete'   # Use environment variable in production

DEBUG = True

ALLOWED_HOSTS = ["*"]   # Add your domain in production


# -----------------------------
# Installed Apps
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'corsheaders',

    # Your apps
    'auths',
    'posts',
]


# -----------------------------
# Middleware (IMPORTANT ORDER!)
# -----------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',   # <-- MUST BE AT TOP
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- after security
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Your JWT Middleware (keep at bottom)
    'auths.middlewares.JWTAuthenticationMiddleware',
]


ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'server.wsgi.application'


# -----------------------------
# Database
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -----------------------------
# Authentication & Passwords
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -----------------------------
# Internationalization
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -----------------------------
# Static Files
# -----------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# -----------------------------
# CORS SETTINGS
# -----------------------------
CORS_ALLOW_ALL_ORIGINS = True   # Allow all frontend origins (Next.js)

CORS_ALLOW_HEADERS = [
    "*"
]

CORS_ALLOW_METHODS = [
    "*"
]

CORS_EXPOSE_HEADERS = ["Authorization"]


# -----------------------------
# Default PK Field
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
