"""
Django settings for votingbooth project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

# Get variables from .env
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'use the google provided details here'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'use the secret key here'
OLD_RECAPTCHA_SECRET_KEY = env('OLD_RECAPTCHA_SECRET_KEY')
RECAPTCHA_SECRET_KEY = env('RECAPTCHA_SECRET_KEY')

# TODO: ACCESS_TOKEN
# ACCESS_TOKEN = env('ACCESS_TOKEN')

# Email

# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))

# https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-EMAIL_FILE_PATH (document for below code)
# SMTP (simple mail transfer protocol) configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')
# go to https://myaccount.google.com/lesssecureapps, log in to your account and make 'Allow less secure apps: ON'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# TODO
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'default': env.db('DATABASE_URL', default='')
}

ALLOWED_HOSTS = ['*']

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# TODO: AUTHENTICATION_BACKENDS

# Application definition

INSTALLED_APPS = [
    'social_django',
    'admin_back',
    'polls',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # admin_back and polls are our custom created apps
    # It is named admin_back because I have encountered some conflicts since Django has its own admin app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'votingbooth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'admin_back/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'votingbooth.wsgi.application'

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'votingbooth/fixtures')
]
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
# TODO: STATIC_ROOT
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "admin_back/static"),
    # 'polls/static/polls',
    # 'admin_back/static/admin_back',
]

# TODO: STATICFILES_STORAGE

# Login Redirect
# _REDIRECT_URL = 'http://127.0.0.1:8000/admin/dashboard/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
