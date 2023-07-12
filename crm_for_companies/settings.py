"""
Django settings for crm_for_companies project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import logging
import os
from pathlib import Path

import cloudinary
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")


ALLOWED_HOSTS = ["*", "localhost", "127.0.0.1", "http://localhost:63342/"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party apps:
    # DJANGO REST APP
    "rest_framework",
    # REST token accounts (python manage.py migrate after this row :) )
    "rest_framework.authtoken",
    # Cloudinary
    "cloudinary",
    # Django Celery Beat
    "django_celery_beat",
    "drf_yasg",
    # Application apps:
    "crm_for_companies.api_companies",
    "crm_for_companies.api_employees",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # next row is enabled after it was disabled for test purposes
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "crm_for_companies.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "crm_for_companies.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "crm_tables",
        "USER": env("DB_USERNAME"),
        "PASSWORD": env("DB_PASSWORD"),
        # Following line works for dockerfile
        # "HOST": "postgres",
        "HOST": env("DB_HOST"),
        # Following line work for local development
        # "HOST": "localhost",
        "PORT": "5432",
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message} {filename} {lineno} : {funcName}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "debug.log"
            ),
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True,
        },
        # For performance reasons, SQL logging is only enabled when settings.DEBUG is set to True, regardless of the
        # logging level or handlers that are installed.
        # 'django.db.backends': {
        #     'handlers': ['file'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 'django.db.backends': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        # }
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
}
# Database logging snippet :
# LOGGING = {
#     'version': 1,
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         }
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#         }
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.accounts.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.accounts.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.accounts.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.accounts.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/' - original
STATIC_URL = "/static/"
# Following row is required for collectstatic command
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

cloudinary.config(
    cloud_name=env("CLOUDINARY_CLOUD_NAME"),
    api_key=env("CLOUDINARY_API_KEY"),
    api_secret=env("CLOUDINARY_API_SECRET"),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        # 'rest_framework.authentication.SessionAuthentication',
        "rest_framework.authentication.TokenAuthentication",
        # 'rest_framework.permissions.IsAuthenticated',
    ],
}

# CSRF_TRUSTED_ORIGINS = ['http://localhost:63342']
# AUTH_USER_MODEL = 'User'

# CELERY settings
# Following two lines work for Docker
# CELERY_BROKER_URL = "pyamqp://guest@rabbitmq//"
# CELERY_RESULT_BACKEND = "db+postgresql://postgres:postgres@postgres/crm_tables"
CELERY_BROKER_URL = env("CELERY_BROKER_URL_")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND_")
# Following two lines work for local dev
# CELERY_BROKER_URL = "pyamqp://guest@localhost//"
# CELERY_RESULT_BACKEND = "db+postgresql://postgres:postgres@localhost/crm_tables"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]

# Swagger settings
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "api_key": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    "DEFAULTS": {
        "OPERATIONS_SORTER": "method",
    },
}

sentry_sdk.init(
    dsn="https://dff33057b335415b9782b9c510f050d6@o4505509751291904.ingest.sentry.io/4505509753257984",
    integrations=[
        DjangoIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
