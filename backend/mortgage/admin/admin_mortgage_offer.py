from django.contrib.admin import register, ModelAdmin

from ..models import MortgageOffer


@register(MortgageOffer)
class MortgageOfferAdmin(ModelAdmin):
    list_display = (
        "bank",
        "min_sum",
        "max_sum",
        "min_term",
        "max_term",
    )
