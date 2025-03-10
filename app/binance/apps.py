
from django.apps import AppConfig



class BinanceConfig(AppConfig):
    name = 'app.binance'

    def ready(self):
        try:
            import app.binance.signals
        except ImportError:
            pass
