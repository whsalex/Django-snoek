# -*- coding: utf-8 -*-
import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'snoek.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'
path = '/srv/www/htdocs'
if path not in sys.path:
    sys.path.append(path)
# in case some 'import only have app name. (without project name)'
path = '/srv/www/htdocs/snoek'
if path not in sys.path:
    sys.path.append(path)
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
