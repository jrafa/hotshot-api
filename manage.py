# -*- coding: utf-8 -*-
"""
    You can run app in shell command: python manage.py runserver
"""
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from api import APP
import settings


MANAGER = Manager(APP)

MANAGER.add_command("runserver", Server(use_debugger=settings.DEBUG, use_reloader=True, host=settings.HOST))

if __name__ == "__main__":
    MANAGER.run()
