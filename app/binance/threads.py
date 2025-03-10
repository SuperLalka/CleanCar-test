import asyncio
import json

from constance import config
from websockets.exceptions import ConnectionClosedError
from websockets.asyncio.client import connect

from app.binance.models import CryptocurrencyTradingPair
from app.binance.tasks import process_stream_message


async def relay(crypto: CryptocurrencyTradingPair) -> None:
    key = crypto.key.lower()
    source_server = f'wss://stream.binance.com:9443/ws/{key}@trade'

    while True:
        try:
            async with connect(source_server) as source_ws:
                while True:
                    message = await source_ws.recv()
                    message = json.loads(message)

                    process_stream_message.delay(
                        message,
                        {
                            'id': crypto.id,
                            'slug': crypto.slug
                        }
                    )
                    await asyncio.sleep(config.REQUEST_FREQUENCY)

        except ConnectionClosedError as err:
            print(err)
            continue


def run_ws():
    async def main():
        tasks = [
            asyncio.create_task(relay(crypto))
            async for crypto in CryptocurrencyTradingPair.objects.filter(is_tracking=True)
        ]
        await asyncio.wait(tasks)

    asyncio.run(main())
