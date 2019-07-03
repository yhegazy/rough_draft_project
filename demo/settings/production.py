from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql.psycopg2',
        'NAME': config('DB_NAME'),
        'USERNAME': config('DB_UNAME'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('HOST'),
        'PORT': ''
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


