from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as filters

from .filters import MortgageFilter
from .models import MortgageOffer
from .serializers import MortgageOfferSerializer


@extend_schema(tags=["Mortgage"])
class MortgageViewSet(ListModelMixin, GenericViewSet):
    """Вьюсет ипотеки."""

    queryset = MortgageOffer.objects.all()
    filterset_class = MortgageFilter

    def get_serializer_class(self):
        if self.action == "list":
            return MortgageOfferSerializer

    def get_queryset(self):
        if self.action == "list":
            request_sum = self.request.query_params["summ"]
            request_term = self.request.query_params["term"]
            return (
                MortgageOffer.objects.select_related("bank")
                .filter(
                    min_sum__lte=request_sum,
                    max_sum__gte=request_sum,
                    min_term__lte=request_term,
                    max_term__gte=request_term,
                )
                .annotate_month_payment(request_sum, request_term)
            )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="summ", description="Сумма ипотеки", required=True, type=OpenApiTypes.INT
            ),
            OpenApiParameter(
                name="term", description="Срок ипотеки", required=True, type=OpenApiTypes.INT
            ),
        ],
        filters=True,
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
