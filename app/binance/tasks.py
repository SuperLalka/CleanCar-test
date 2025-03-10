from datetime import datetime

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from config.celery_app import app
from django.contrib.auth import get_user_model

from app.binance.models import CryptocurrencyCostSnapshotLog

User = get_user_model()


@app.task
def process_stream_message(message: dict, crypto_data: dict):
    if message.get('e') == 'trade':
        CryptocurrencyCostSnapshotLog.objects.create(
            value=message.get('p'),
            created_at=datetime.fromtimestamp(message.get('T') / 1000),
            crypto_id=crypto_data['id']
        )

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            crypto_data['slug'],
            {
                'type': 'chat.message',
                'message': message
            }
        )
