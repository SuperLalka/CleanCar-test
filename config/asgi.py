
import os
import django

import threading

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from config import websocket_urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "https": get_asgi_application(),
        "websocket": URLRouter(websocket_urls.websocket_urlpatterns),
    }
)


from app.binance import threads as binance_threads
threading.Thread(target=binance_threads.run_ws).start()
