"""
Django settings for VolunteerManager project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# location=1 #'Local'
# location=2 #'Staging'
location=3 #'Production'

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
MEDIA_ROOT = 'media'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3_%%8#6+dz4*mosz#k8!t8nv+47mau92$rcl2#!3e=c@+t21od'

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
#DEFAULT APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
#THIRD PARTY APPS
    'registration',
        #Copyright (c) 2007-2012, James Bennett
        #All rights reserved.
    'guardian',
    'favicon',
    'django.contrib.sites',
    
    
#LOCAL APPS
    'Volunteer'
)

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window;
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

ROOT_URLCONF = 'VolunteerManager.urls'

ANONYMOUS_USER_ID = -1

WSGI_APPLICATION = 'VolunteerManager.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Parse database configuration from $DATABASE_URL

if location== 1: #Local
    DEBUG = True
    TEMPLATE_DEBUG = True
    DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'djangostack',
             'USER': 'root',
             'PASSWORD': 'jolliko9',
             'HOST': 'localhost',     
             'PORT': '3306',
         }
    }
    
elif location== 2:  #Staging   
    DEBUG = True
    TEMPLATE_DEBUG = True
    import dj_database_url
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config() 
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    
elif location==3: #'production':
    DEBUG = False
    TEMPLATE_DEBUG = False
    import dj_database_url
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config() 
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

LOGIN_REDIRECT_URL = '/home/'

SITE_ID = 1