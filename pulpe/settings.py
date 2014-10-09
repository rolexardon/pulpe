# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'asccoo@3!v0pr6ek*2s@zuobha0iol6^w!r@86s41yj*x3s#gd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'clientes',
	'inventario',
	'facturas',
#	'south',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_DIRS = (
	os.path.join(SITE_ROOT, 'templates'),
	os.path.join(BASE_DIR, 'inventario/templates'),
)

ROOT_URLCONF = 'pulpe.urls'
WSGI_APPLICATION = 'pulpe.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {

'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', 
            'NAME': 'csdfs',
            'USER': 'csdfsusr',
            'PASSWORD': 'f33dingc$d',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '5432',                      # Set to empty string for default.
        }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATICFILES_FINDERS =(
#	'django.contrib.staticfiles.finders.FileSystemFinder',
# 	'django.contrib.staticfiles.finders.AppDirectoriesFinder'
#)

STATICFILES_DIRS = (
	os.path.join(BASE_DIR,'pulpe/resources'),
)

#STATIC_URL = '/resources/'

STATIC_ROOT =  '/home/rolexardon/webapps/media_csdfs/'
STATIC_URL = '/media_csdfs/'


#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'rolando.ardon299@gmail.com'
#EMAIL_HOST_PASSWORD = 'dwdrumming1'

#EMAIL_BACKEND = 'webfaction.backends.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_PORT = 25
#EMAIL_USE_TLS = False

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'billing_csdfoodshop'
EMAIL_HOST_PASSWORD = 'dwdrumming'
DEFAULT_FROM_EMAIL = 'billing@csdfoodshop.rolexardon.webfactional.com'
