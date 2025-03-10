from typing import Type

from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver

from app.binance.models import CryptocurrencyTradingPair


@receiver(pre_save, sender=CryptocurrencyTradingPair)
@transaction.atomic
def cryptocurrency_trading_pair_pre_save(
    sender: Type[CryptocurrencyTradingPair],
    instance: CryptocurrencyTradingPair,
    **kwargs
):
    if instance.pk is None:
        instance.slug = instance.key.lower()

    else:
        if instance.slug != instance.key.lower():
            instance.slug = instance.key.lower()
