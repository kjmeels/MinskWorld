from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from properties.models import Apartment
from .likes import Like


@extend_schema(tags=["Likes"])
class LikeViewSet(GenericViewSet):
    def list(self, request, *args, **kwargs):
        likes = Like(request.session)
        return Response(likes.keys)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="apartment_id", description="id квартиры", required=True, type=OpenApiTypes.INT
            )
        ]
    )
    @action(detail=False, methods=["POST"])
    def add_like(self, request, *args, **kwargs):
        if apartment_id := request.query_params.get("apartment_id"):
            if Apartment.objects.filter(id=int(apartment_id)).exists():
                likes = Like(request.session)
                likes.add(pk=int(apartment_id))
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="apartment_id", description="id квартиры", required=True, type=OpenApiTypes.INT
            )
        ]
    )
    @action(detail=False, methods=["DELETE"])
    def destroy_like(self, request, *args, **kwargs):
        if apartment_id := request.query_params.get("apartment_id"):
            if Apartment.objects.filter(id=int(apartment_id)).exists():
                likes = Like(request.session)
                likes.remove(pk=int(apartment_id))
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["DELETE"])
    def clear_like(self, request, *args, **kwargs):
        likes = Like(request.session)
        likes.clear()
        return Response(status=status.HTTP_204_NO_CONTENT)
