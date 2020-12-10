import os

from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
os.environ["DJANGO_SETTINGS_MODULE"] = "server.settings.base"

application = get_asgi_application()
