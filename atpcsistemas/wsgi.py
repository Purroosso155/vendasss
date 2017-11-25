"""
WSGI config for atpcsistemas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('C:/Users/ATPC-Sistemas/Bitnami Django Stack projects/atpcsistemas')
os.environ.setdefault("PYTHON_EGG_CACHE", "C:/Users/ATPC-Sistemas/Bitnami Django Stack projects/atpcsistemas/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "atpcsistemas.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
