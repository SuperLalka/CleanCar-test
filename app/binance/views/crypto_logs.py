
from typing import Union

from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.request import Request
from rest_framework.response import Response

from app.binance.filters import CryptoLogsFilter
from app.binance.models import CryptocurrencyCostSnapshotLog
from app.binance.serializers import CryptoLogSerializer, RetrieveCryptoLogSerializer
from app.utils.pagination import ExtendedPageNumberPagination


class CryptoLogListPageView(generics.ListAPIView):
    queryset = CryptocurrencyCostSnapshotLog.objects.order_by('-created_at')
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = RetrieveCryptoLogSerializer
    template_name = 'pages/crypto/logs-list.html'
    pagination_class = ExtendedPageNumberPagination
    filterset_class = CryptoLogsFilter


class CryptoLogViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = CryptocurrencyCostSnapshotLog.objects.all()
    serializer_class = CryptoLogSerializer
    filterset_class = CryptoLogsFilter

    def get_queryset(self):
        self.queryset = super().get_queryset() \
            .select_related('crypto') \
            .order_by('-created_at')
        return self.filter_queryset(self.queryset)

    def list(self, request: Request, *args, **kwargs) -> Response:
        self.serializer_class = RetrieveCryptoLogSerializer
        return super().list(self, request, *args, **kwargs)

    def retrieve(self, request: Request, pk: Union[int, str] = None) -> Response:
        instance = get_object_or_404(self.get_queryset(), pk=pk)
        response_data = RetrieveCryptoLogSerializer(instance).data
        return Response(response_data, status=status.HTTP_200_OK)
