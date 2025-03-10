
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views import defaults as default_views
from django.views.generic.base import RedirectView

from app.binance import views as binance_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('config.api_router')),

    path('crypto/', binance_views.CryptoListPageView.as_view(), name='crypto-list-page'),
    path('crypto/<slug:slug>/', binance_views.CryptoDetailPageView.as_view(), name='crypto-detail-page'),
    path('crypto_logs/', binance_views.CryptoLogListPageView.as_view(), name='crypto-logs-list-page'),
    path('', RedirectView.as_view(url='crypto', permanent=False), name='home'),
]

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += [
        path(
            '400/',
            default_views.bad_request,
            kwargs={'exception': Exception("Bad Request!")},
        ),
        path(
            '403/',
            default_views.permission_denied,
            kwargs={'exception': Exception("Permission Denied")},
        ),
        path(
            '404/',
            default_views.page_not_found,
            kwargs={'exception': Exception("Page not Found")},
        ),
        path('500/', default_views.server_error),
    ] + debug_toolbar_urls()
