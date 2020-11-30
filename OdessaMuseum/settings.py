"""
Django settings for OdessaMuseum project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2j$!^9nanfs*8lpgpz!zty$1bg4zbd=2m*#)%f0%qaqmequ+v3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'ortniter.pythonanywhere.com',
]

# Application definition


INSTALLED_APPS = [
    'ofam_api.apps.OfamApiConfig',
    'ofam_telegram.apps.OfamTelegramConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_telegrambot',
    'ckeditor',
    'adminsortable',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OdessaMuseum.urls'

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
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'OdessaMuseum.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

import os

STATIC_URL = '/static/'
# STATICFILES_DIRS = [
# BASE_DIR / "static"
# ]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Django Telegram Bot settings

DJANGO_TELEGRAMBOT = {

    'MODE': 'WEBHOOK',  # (Optional [str]) # The default value is WEBHOOK,
    # otherwise you may use 'POLLING'
    # NB: if use polling you must provide to run
    # a management command that starts a worker

    'WEBHOOK_SITE': 'ortniter.pythonanywhere.com',
    # 'WEBHOOK_PREFIX': '/prefix',  # (Optional[str]) # If this value is specified,
    # a prefix is added to webhook url

    'WEBHOOK_CERTIFICATE' : 'cert.pem', # If your site use self-signed
    # certificate, must be set with location of your public key
    # certificate.(More info at https://core.telegram.org/bots/self-signed )

    'STRICT_INIT': True,  # If set to True, the server will fail to start if some of the
    # apps contain telegrambot.py files that cannot be successfully
    # imported.

    'BOTS': [
        {
            'TOKEN': '1270547075:AAHb_afunhhW2CWQrZ84NWYCbvHVz-AoYNk',  # Your bot token.

            # 'ALLOWED_UPDATES':(Optional[list[str]]), # List the types of
            # updates you want your bot to receive. For example, specify
            # ``["message", "edited_channel_post", "callback_query"]`` to
            # only receive updates of these types. See ``telegram.Update``
            # for a complete list of available update types.
            # Specify an empty list to receive all updates regardless of type
            # (default). If not specified, the previous setting will be used.
            # Please note that this parameter doesn't affect updates created
            # before the call to the setWebhook, so unwanted updates may be
            # received for a short period of time.

            # 'TIMEOUT':(Optional[int|float]), # If this value is specified,
            # use it as the read timeout from the server

            # 'WEBHOOK_MAX_CONNECTIONS':(Optional[int]), # Maximum allowed number of
            # simultaneous HTTPS connections to the webhook for update
            # delivery, 1-100. Defaults to 40. Use lower values to limit the
            # load on your bot's server, and higher values to increase your
            # bot's throughput.

            # 'MESSAGEQUEUE_ENABLED':(Optinal[bool]), # Make this True if you want to use messagequeue

            # 'MESSAGEQUEUE_ALL_BURST_LIMIT':(Optional[int]), # If not provided 29 is the default value

            # 'MESSAGEQUEUE_ALL_TIME_LIMIT_MS':(Optional[int]), # If not provided 1024 is the default value

            # 'MESSAGEQUEUE_REQUEST_CON_POOL_SIZE':(Optional[int]), # If not provided 8 is the default value

            # 'POLL_INTERVAL' : (Optional[float]), # Time to wait between polling updates from Telegram in
            # seconds. Default is 0.0

            # 'POLL_CLEAN':(Optional[bool]), # Whether to clean any pending updates on Telegram servers before
            # actually starting to poll. Default is False.

            # 'POLL_BOOTSTRAP_RETRIES':(Optional[int]), # Whether the bootstrapping phase of the `Updater`
            # will retry on failures on the Telegram server.
            # |   < 0 - retry indefinitely
            # |     0 - no retries (default)
            # |   > 0 - retry up to X times

            # 'POLL_READ_LATENCY':(Optional[float|int]), # Grace time in seconds for receiving the reply from
            # server. Will be added to the `timeout` value and used as the read timeout from
            # server (Default: 2).
        },
        # Other bots here with same structure.
    ],

}
