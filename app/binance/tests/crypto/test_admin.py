
from django.test import TestCase, Client
from django.urls import reverse
from model_bakery import baker

from app.binance.models import CryptocurrencyTradingPair
from app.users.models import User
from app.utils.utils import get_random_uuid_hex


class CryptocurrencyTradingPairAdminTestCase(TestCase):
    def setUp(self):
        super().setUp()

        self.super_user = User.objects.create_superuser(
            email='admin@example.com',
            password='secret',
        )
        self.client = Client()
        self.client.login(email='admin@example.com', password='secret')

        self.user = User.objects.create_user(
            email='test_user@example.com',
            password='secret',
        )

        self.crypto = baker.make(
            'binance.CryptocurrencyTradingPair',
            **{
                'key': 'btcfake',
                'is_tracking': False,
            }
        )

    def test_changelist_crypto(self):
        url = reverse('admin:binance_cryptocurrencytradingpair_changelist')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_search_crypto(self):
        url = reverse('admin:binance_cryptocurrencytradingpair_changelist')
        response = self.client.get(url, data={'q': 'test'})
        assert response.status_code == 200

    def test_add_crypto(self):
        url = reverse('admin:binance_cryptocurrencytradingpair_add')
        response = self.client.get(url)
        assert response.status_code == 200

        response = self.client.post(
            url,
            data={
                'key': 'btc2fake',
                'slug': str(get_random_uuid_hex()),
                'description': '',
                'is_tracking': False,
            },
        )

        assert response.status_code == 302
        assert CryptocurrencyTradingPair.objects.filter(key='btc2fake').exists()

    def test_view_crypto(self):
        url = reverse('admin:binance_cryptocurrencytradingpair_change', kwargs={'object_id': self.crypto.id})
        response = self.client.get(url)
        assert response.status_code == 200
