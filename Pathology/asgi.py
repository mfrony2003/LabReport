"""
ASGI config for Pathology project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application



if os.environ.get("DEBUG")=="True":
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.Settings.localSettings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.Settings.prodSettings')





application = get_asgi_application()
