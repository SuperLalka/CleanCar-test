
from django.views import generic

from app.binance.models import CryptocurrencyTradingPair


class CryptoDetailPageView(generic.DetailView):
    model = CryptocurrencyTradingPair
    template_name = 'pages/crypto/detail.html'
    slug_field = 'slug'


class CryptoListPageView(generic.ListView):
    model = CryptocurrencyTradingPair
    template_name = 'pages/crypto/list.html'
