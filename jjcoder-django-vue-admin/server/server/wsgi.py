import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
os.environ["DJANGO_SETTINGS_MODULE"] = "server.settings.base"

application = get_wsgi_application()
