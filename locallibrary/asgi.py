"""
ASGI config for locallibrary project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')

# application = get_asgi_application()

# myproject/asgi.py

import os
from django.core.asgi import get_asgi_application
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi_app import app as fastapi_app
# import fastapi_app
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

django_app = get_asgi_application()
app = WSGIMiddleware(django_app)
app.mount("/api", fastapi_app)
