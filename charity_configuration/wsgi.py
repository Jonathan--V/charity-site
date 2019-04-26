"""
WSGI config for CharitySite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

test_mode = os.environ.get('charity_site_is_test_mode')
if test_mode and 'test' in test_mode:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charity_configuration.test_settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charity_configuration.dev_settings')

application = get_wsgi_application()
