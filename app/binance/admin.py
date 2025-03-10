from django.contrib import admin
from django.db.models import Case, Value, When

from app.binance.models import (
    CryptocurrencyCostSnapshotLog,
    CryptocurrencyTradingPair,
)


@admin.register(CryptocurrencyTradingPair)
class CryptocurrencyTradingPairAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'slug', 'is_tracking', 'description']
    list_display_links = list_display[:2]
    list_filter = ['is_tracking']
    ordering = ['key']
    search_fields = ['key']

    actions = ['switch_tracking']

    def switch_tracking(self, request, queryset):
        queryset.update(is_tracking=Case(
            When(is_tracking=True, then=Value(False)),
            When(is_tracking=False, then=Value(True)),
        ))


@admin.register(CryptocurrencyCostSnapshotLog)
class CryptocurrencyCostSnapshotLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'crypto', 'created_at', 'value']
    list_filter = ['crypto']
    ordering = ['-created_at']
    raw_id_fields = ['crypto']
    readonly_fields = ['created_at']

    def has_add_permission(self, request):
        return False
