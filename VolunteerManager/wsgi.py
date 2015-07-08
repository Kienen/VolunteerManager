"""
WSGI config for VolunteerManager project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VolunteerManager.settings")

from django.core.wsgi import get_wsgi_application
location=3

if location==1:
    application = get_wsgi_application()
else:
    from dj_static import Cling
    application = Cling(get_wsgi_application())
