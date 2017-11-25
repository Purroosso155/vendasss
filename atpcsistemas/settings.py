"""
Django settings for atpcsistemas project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2g!z)j@ilsq-0yk187$u0d1#7^6lnznntr%1#2^b+^0tlymget'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [ '*']

USE_X_FORWARDED_HOST = True


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contas',
    'SalesSystem',
    'meusite',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'atpcsistemas.urls'

WSGI_APPLICATION = 'atpcsistemas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'SalesSystem.db'),
    }
}

# use esta parte para banco de dados mysql
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome do banco de dados',
        'HOST': 'local do banco de dados',
        'PORT': '3306',
        'USER': 'root', # caso tenha um usuario diferente de root mude esta opcao
        'PASSWORD': 'senha'
    }
}
"""

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth'
    'django.core.context_processors.debug'
    'django.core.context_processors.i18n'
    'django.core.context_processors.media'
    'django.core.context_processors.request'
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'contas/templates'),
    os.path.join(BASE_DIR, 'SalesSystem/templates'),
    os.path.join(BASE_DIR, 'meusite/templates/python'),
    os.path.join(BASE_DIR, 'meusite/templates/django'),
    os.path.join(BASE_DIR, 'meusite/templates/android'),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin_media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


LOGIN_REDIRECT_URL = '/SalesSystem/'
LOGIN_URL = '/entrar/'
LOGOUT_URL = '/sair/'


EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[]'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

