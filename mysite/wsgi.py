"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
application = get_wsgi_application()


# add the following lines to serve static files
# from django.conf import settings
# from django.contrib.staticfiles.handlers import StaticFilesHandler
# application = StaticFilesHandler(get_wsgi_application())
