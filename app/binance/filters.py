
from django_filters import rest_framework as filters

from app.binance.models import CryptocurrencyCostSnapshotLog


class CryptoLogsFilter(filters.FilterSet):
    created_gte = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_lte = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    crypto_id = filters.NumberFilter(field_name='crypto')
    crypto_slug = filters.CharFilter(field_name='crypto__slug', lookup_expr='icontains')

    class Meta:
        model = CryptocurrencyCostSnapshotLog
        fields = ['created_at', 'crypto']
