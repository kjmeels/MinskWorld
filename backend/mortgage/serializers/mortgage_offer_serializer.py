from rest_framework import serializers

from mortgage.models import MortgageOffer
from .mortgage_bank_serializer import MortgageBankSerializer


class MortgageOfferSerializer(serializers.ModelSerializer):
    bank = MortgageBankSerializer()
    month_payment = serializers.IntegerField()

    class Meta:
        model = MortgageOffer
        fields = (
            "bank",
            "month_payment",
            "max_sum",
            "max_term",
            "rate",
            "type",
        )
