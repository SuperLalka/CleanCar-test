from unittest import TestCase

from django.urls import resolve, reverse


class CryptocurrencyTradingPairUrlsTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.crypto_slug = 'btcfake'

    def test_crypto_detail(self):
        assert (
            reverse('crypto-detail-page', kwargs={'slug': self.crypto_slug})
            == f'/crypto/{self.crypto_slug}/'
        )
        assert resolve(f'/crypto/{self.crypto_slug}/').view_name == 'crypto-detail-page'

    def test_crypto_list(self):
        assert reverse('crypto-list-page') == '/crypto/'
        assert resolve('/crypto/').view_name == 'crypto-list-page'
