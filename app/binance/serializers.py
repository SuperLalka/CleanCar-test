from rest_framework import serializers

from app.binance.models import CryptocurrencyCostSnapshotLog


class CryptoLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = CryptocurrencyCostSnapshotLog
        fields = '__all__'


class RetrieveCryptoLogSerializer(CryptoLogSerializer):
    pass
