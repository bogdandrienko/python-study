"""
Django settings for django_settings project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    SECRET_KEY=(str, "1 secret_key 1"),
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(str, ""),
    CORS_ALLOW_ALL_ORIGINS=(bool, False),
    CORS_URLS_REGEX=(str, ""),
    SQL_ENGINE=(str, "django.db.backends.sqlite3"),
    SQL_DATABASE=(str, "database/db.sqlite3"),
    SQL_USER=(str, "django_user"),
    SQL_PASSWORD=(str, "12345"),
    SQL_HOST=(str, "127.0.0.1"),
    SQL_PORT=(str, "5432"),
    REDIS_LOCATION=(str, "rediss://12345@127.0.0.1:3697/0"),
)

environ.Env.read_env(os.path.join(BASE_DIR, 'django_settings/.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]
CORS_ALLOW_ALL_ORIGINS = env('CORS_ALLOW_ALL_ORIGINS')
if env('CORS_URLS_REGEX') == "*":
    CORS_URLS_REGEX = r"^/.*"
elif env('CORS_URLS_REGEX') == "":
    pass
else:
    CORS_URLS_REGEX = env('CORS_URLS_REGEX')

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:8000",
#     "http://localhost:3000",

#     "http://127.0.0.1:8000",
#     "http://127.0.0.1:3000",
# ]

# Application definition

INSTALLED_APPS = [
    'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',

    'django_app',
    'django_drf_todo_list',
    'django_mvt_todo_list',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'django_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', BASE_DIR / 'frontend'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.request',

                'django_mvt_todo_list.context_processors.todo_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000

SQL_ENGINE = env("SQL_ENGINE")
if SQL_ENGINE == "django.db.backends.sqlite3":
    SQL_DATABASE = Path(BASE_DIR, env("SQL_DATABASE"))
else:
    SQL_DATABASE = env("SQL_DATABASE")
SQL_USER = env("SQL_USER")
SQL_PASSWORD = env("SQL_PASSWORD")
SQL_HOST = env("SQL_HOST")
SQL_PORT = env("SQL_PORT")

DATABASES = {
    "default": {
        "ENGINE": SQL_ENGINE,
        "NAME": SQL_DATABASE,
        "USER": SQL_USER,
        "PASSWORD": SQL_PASSWORD,
        "HOST": SQL_HOST,
        "PORT": SQL_PORT,
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django_db',
#         'USER': 'django_usr',
#         'PASSWORD': '12345qwertY!',
#         'HOST': '127.0.0.1',  # localhost
#         'PORT': '3306',
#     }
# }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'special': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
        'TIMEOUT': '120',
        'OPTIONS': {
            # "MAX_ENTIES": 200,
        }
    },
    # 'extra': {
    #     'BACKEND': 'django_redis.cache.RedisCache',
    #     'LOCATION': env("REDIS_LOCATION")',
    #     'TIMEOUT': '240',
    #     'OPTIONS': {
    #         # "MAX_ENTIES": 200,
    #         "PASSWORD": "12345qwertY!"
    #     }
    # }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-US'
LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Etc/GMT-6'
# TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
if DEBUG:
    STATICFILES_DIRS = [
        Path(BASE_DIR, 'static'),
        Path(BASE_DIR, 'static_external'),
        Path(BASE_DIR, 'django_mvt_todo_list/static'),
        Path(BASE_DIR, 'frontend/public/static'),
        Path(BASE_DIR, 'frontend/build/static'),
    ]
else:
    STATIC_ROOT = Path(BASE_DIR, 'static')
    STATICFILES_DIRS = [
        Path(BASE_DIR, 'static_external'),
        Path(BASE_DIR, 'django_mvt_todo_list/static'),
        Path(BASE_DIR, 'frontend/build/static'),
    ]

# heroku
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# heroku

MEDIA_URL = 'media/'
MEDIA_ROOT = Path(BASE_DIR, 'static/media')


# celery.py
CELERY_APP_TIMEZONE = 'Asia/Almaty'
CELERY_APP_TASK_TRACK_STARTED = True
CELERY_APP_TASK_TIME_LIMIT = 1800

CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
# CELERY_BROKER_URL = "amqp://myuser:mypassword@localhost:5672/myvhost"
# CELERY_RESULT_BACKEND = "redis://localhost:6379"

# BROKER_URL = "redis://localhost:6379"
# RESULT_BACKEND = "redis://localhost:6379"
# CELERY_APP_BROKER_URL = "redis://localhost:6379"
# CELERY_APP_RESULT_BACKEND = "redis://localhost:6379"
# celery.py


# email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# FROM_EMAIL = 'bogdandrienko@gmail.com'
# EMAIL_ADMIN = 'bogdandrienko@gmail.com'
#
# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_HOST_USER = 'eevee.cycle'
# EMAIL_HOST_PASSWORD = '31284bogdan'
# EMAIL_PORT = 465
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True
#
# host: EMAIL_HOST
# port: EMAIL_PORT
# username: EMAIL_HOST_USER
# password: EMAIL_HOST_PASSWORD
# use_tls: EMAIL_USE_TLS
# use_ssl: EMAIL_USE_SSL
# email

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# drf
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAdminUser',
#         # 'rest_framework.permissions.IsAuthenticated',
#         # 'rest_framework.permissions.AllowAny',
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
# }
# from rest_framework.parsers import JSONParser, MultiPartParser
# REST_FRAMEWORK = {
#     'DEFAULT_PARSER_CLASSES': [
#         # 'rest_framework.parsers.JSONParser',
#         'rest_framework.parsers.MultiPartParser',
#     ]
# }
# drf

# jwt
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=2),
#     'ROTATE_REFRESH_TOKENS': True,
#     'BLACKLIST_AFTER_ROTATION': True,
#     'UPDATE_LAST_LOGIN': True,
#
#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,
#     'JWK_URL': None,
#     'LEEWAY': 0,
#
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
#     'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
#
#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',
#     'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
#
#     'JTI_CLAIM': 'jti',
#
#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(days=1),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=2),
# }
# jwt
