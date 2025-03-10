from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.binance import views as binance_views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('crypto_logs', binance_views.CryptoLogViewSet, basename='crypto-logs')


app_name = 'api'
urlpatterns = router.urls
