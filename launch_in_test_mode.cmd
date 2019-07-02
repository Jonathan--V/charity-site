@echo off
CALL "venv/Scripts/activate.bat"
py charity_configuration/test_database_setup.py
py manage.py runserver --settings=charity_configuration.test_settings
CALL "venv/Scripts/deactivate.bat"