from rest_framework import serializers

from mortgage.models import MortgageBank


class MortgageBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = MortgageBank
        fields = (
            "id",
            "name",
            "slug",
            "logo",
        )
