import json
import random
import secrets
from unittest import mock

from channels_redis.core import RedisChannelLayer
from constance.test import override_config
from model_bakery import baker
from rest_framework.test import APITestCase
from websockets.sync.client import connect

from app.binance.models import CryptocurrencyCostSnapshotLog
from app.binance.tasks import process_stream_message


class CryptocurrencyTradingPairTasksTestCase(APITestCase):
    def setUp(self) -> None:
        super().setUp()

        self.user = baker.make(
            'users.User',
            **{
                'email': 'tester@test.com',
                'password': secrets.token_hex(16),
            }
        )

        self.crypto = baker.make(
            'binance.CryptocurrencyTradingPair',
            **{
                'key': 'btcusdt',
                'is_tracking': False,
            }
        )

    @override_config(REQUEST_FREQUENCY=1)
    @mock.patch.object(RedisChannelLayer, 'group_send')
    def test_process_stream_message_task(self, channel_layer_mock):
        source_server = f'wss://stream.binance.com:9443/ws/{self.crypto.slug}@trade'
        LOGS_COUNT = random.randint(3, 7)

        for _ in range(LOGS_COUNT):
            with connect(source_server) as source_ws:
                while True:
                    message = source_ws.recv()
                    message = json.loads(message)

                    process_stream_message(
                        message,
                        {
                            'id': self.crypto.id,
                            'slug': self.crypto.slug
                        }
                    )

                    assert channel_layer_mock.called
                    channel_layer_mock_args_list = channel_layer_mock.call_args_list
                    call_args, _ = channel_layer_mock_args_list[0]

                    assert call_args[0] == self.crypto.slug
                    assert call_args[1] == {
                        'type': 'chat.message',
                        'message': message
                    }
                    channel_layer_mock.reset_mock()

                    self.assertTrue(
                        CryptocurrencyCostSnapshotLog.objects
                            .filter(crypto=self.crypto, value=message['p'])
                            .exists()
                    )
                    break

        self.assertTrue(
            CryptocurrencyCostSnapshotLog.objects.all().count(), LOGS_COUNT
        )
