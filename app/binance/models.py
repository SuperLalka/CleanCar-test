
from django.db import models

from app.utils.utils import get_random_uuid_hex


class CryptocurrencyTradingPair(models.Model):
    key = models.CharField(max_length=20)
    slug = models.SlugField(
        max_length=32,
        unique=True,
        db_index=True,
        default=get_random_uuid_hex
    )
    description = models.TextField(blank=True, null=True)
    is_tracking = models.BooleanField(default=False)

    class Meta:
        db_table = 'crypto_trading_pair'
        verbose_name = 'Cryptocurrency Trading Pair'
        verbose_name_plural = 'Cryptocurrency Trading Pairs'

    def __str__(self):
        return self.key


class CryptocurrencyCostSnapshotLog(models.Model):
    # https://developers.binance.com/docs/binance-spot-api-docs/user-data-stream
    """
    "e": Event type
    "E": Event Time
    "s": Symbol
    "t": Trade ID
    "p": Order price
    "q": Order quantity
    "T": Transaction time
    "m": Is this trade the maker side?
    "M": Ignore
    """
    value = models.DecimalField(max_digits=28, decimal_places=8)
    created_at = models.DateTimeField()

    crypto = models.ForeignKey(
        CryptocurrencyTradingPair,
        on_delete=models.CASCADE,
        related_name='cost_snapshot_log',
    )

    class Meta:
        db_table = 'crypto_cost_snapshot_log'
        verbose_name = 'Cryptocurrency Cost Snapshot Log'
        verbose_name_plural = 'Cryptocurrency Cost Snapshot Logs'

    def __str__(self):
        return f"{self.crypto} / {self.created_at}"
