#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    test_mode = os.environ.get('charity_site_is_test_mode')
    if test_mode and 'test' in test_mode:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charity_configuration.test_settings')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charity_configuration.dev_settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
