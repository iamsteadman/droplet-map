try:
	import newrelic.agent
	newrelic.agent.initialize('newrelic.ini')
except ImportError:
	pass

import os, sys
import django.core.handlers.wsgi

sys.path.insert(0, os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'droplet.settings'
os.environ['PYTHON_EGG_CACHE'] = os.path.dirname(__file__) + '/.python-eggs'
application = django.core.handlers.wsgi.WSGIHandler()